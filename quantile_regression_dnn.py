import tensorflow as tf
#from tensorflow import tf.keras

#from tensorflow.tf.keras import Model
#from tensorflow.tf.keras import load_model
#from tensorflow.tf.keras.layers import Input, Activation, Dense, Lambda
#from tensorflow.tf.keras import backend as K
#from tensorflow.tf.keras.optimizers import Adam
#from tensorflow.tf.keras.callbacks import EarlyStopping, ReduceLROnPlateau, TerminateOnNaN


import numpy as np


class Quantile_Regression( object ):
    
    Mjj_selection = 1100.
    Mjj_scaling = 2000.0
    
    def __init__(self,quantile):
        self.quantile = quantile
        self.model = self.build()


    def quantile_loss( self ):
        def loss( target, pred ):
            alpha = 1 - self.quantile
            err = target - pred
            return tf.where(err>=0, alpha*err, (alpha-1)*err)
        return loss

    def build( self ):
        num_nodes_per_layer = 100
        self.inputs = tf.keras.Input(shape=(1,))
        self.first_hidden = tf.keras.layers.Dense(num_nodes_per_layer, activation='relu')(self.inputs)
        hidden = tf.keras.layers.Dense(num_nodes_per_layer, activation='relu')(self.first_hidden)
        hidden = tf.keras.layers.Dense(num_nodes_per_layer, activation='relu')(hidden)
        hidden = tf.keras.layers.Dense(num_nodes_per_layer, activation='relu')(hidden)
        self.output = tf.keras.layers.Dense(1)(hidden)
        model = tf.keras.Model(self.inputs, self.output)
        self.compile_model( model )
        model.summary()
        return model
    
    
    def compile_model( self, model ):
        model.compile(loss=self.quantile_loss(), optimizer='Adam') # Adam(lr=1e-4) TODO: add learning rate
    

    def fit( self, x, y ):
        xx = np.reshape( self.scaleDownMjj(x), (-1,1) )
        self.model.fit( xx, y, epochs=100, batch_size=128, verbose=2, validation_split=0.2, shuffle=True, \
            callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1),tf.keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=3, verbose=1)])
        

    def predict( self, mjj ):
        xx = np.reshape( self.scaleDownMjj(mjj), (-1,1) )
        return self.model.predict( xx )
            
    def scaleDownMjj( self, x ):
        return x
        #return (x-2*self.Mjj_selection)/self.Mjj_scaling
    
    def select_events( self, mjj, loss ):
        cut = self.predict( mjj )
        return loss > cut.flatten()
    
    def save( self, path ):
        self.model.save( path )
        
    def load( self, path ):
        self.model = tf.keras.models.load_model( path, custom_objects={'loss':tf.keras.losses.mean_squared_error} ) # TODO: do sth about the loss dummy -> remove function closure of loss
        
        
class Overflow_Bin_Layer( tf.keras.layers.Layer ):
        
        def __init__(self, max_mjj, **kwargs):
            super(Overflow_Bin_Layer, self).__init__(**kwargs)
            self.max_mjj = max_mjj

        def build( self, input_shape ):
            self.max_mjj_tensor = tf.constant( self.max_mjj, dtype=tf.float32)
            
        def call( self, x_mjj ):
            return tf.keras.backend.minimum( x_mjj, self.max_mjj_tensor )
        
        def get_config( self ):
            config = super(Overflow_Bin_Layer, self).get_config()
            config.update({"max_mjj": self.max_mjj})
            return config
        
        
class Quantile_Regression_Overflow_Bin( Quantile_Regression ):
        
    def fit( self, x, y ):
        super( Quantile_Regression_Overflow_Bin, self ).fit( x, y )
         # get overflow bin (max accepted mjj) for regression cut
        sel = self.select_events( x, y ) # get selection for qcd training set
        print(x.shape)
        print(x[sel].shape)
        self.max_acc_mjj = np.max(x[sel]) # get max mjj in accepted set
        self.overflow_cut = self.predict( self.max_acc_mjj ).item() # get loss cut value at max mjj accepted
        print('cut point: (', self.max_acc_mjj, ',', self.overflow_cut, ')')
        # add additional overflow layer
        self.add_overflow_layer(self.max_acc_mjj)
       
    def add_overflow_layer( self, max_acc_mjj ):
        #overflow_bin_layer = Overflow_Bin_Layer( max_acc_mjj )(self.model.layers[-1].output)
        overflow_bin_layer = Overflow_Bin_Layer( max_acc_mjj )( self.model.input ) # reroute inputs to max-mjj-cutting layer
        self.first_hidden = self.first_hidden( overflow_bin_layer )
        self.model = tf.keras.Model(self.inputs,self.output)
        self.compile_model( self.model ) 
        self.model.summary()
        
    def load( self, path ):
        self.model = tf.keras.models.load_model( path, custom_objects={'Overflow_Bin_Layer':Overflow_Bin_Layer, 'loss':tf.keras.losses.mean_squared_error} ) # TODO: do sth about the loss dummy -> remove function closure of loss
                                       