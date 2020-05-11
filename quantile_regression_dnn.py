from keras.models import Model, load_model
from keras.layers import Input, Activation, Dense
from keras.callbacks import EarlyStopping
from keras import backend as K
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, TerminateOnNaN

import numpy as np


class Quantile_Regression( ):
    
    Mjj_selection = 1100.
    Mjj_scaling = 2000.0
    
    def __init__(self,quantile):
        self.quantile = quantile
        self.model = self.build()


    def quantile_loss( self ):
        def loss( target, pred ):
            alpha = 1 - self.quantile
            err = target - pred
            return K.tf.where(err>=0, alpha*err, (alpha-1)*err)
        return loss

    def build( self ):

        inputs = Input(shape=(1,))
        hidden = Dense(50, activation='relu')(inputs)
        hidden = Dense(50, activation='relu')(hidden)
        hidden = Dense(50, activation='relu')(hidden)
        hidden = Dense(50, activation='relu')(hidden)
        output = Dense(1)(hidden)
        model = Model(inputs, output)
        model.compile(loss=self.quantile_loss(), optimizer=Adam(lr=1e-4))
        model.summary()
        return model


    def fit( self, x, y ):
        xx = np.reshape( self.scaleDownMjj(x), (-1,1) )
        self.model.fit( xx, y, epochs=100, batch_size=128, verbose=0, validation_split=0.2, shuffle=True, \
            callbacks=[EarlyStopping(monitor='val_loss', patience=10, verbose=1),ReduceLROnPlateau(factor=0.2, patience=3, verbose=1)])
        

    def predict( self, mjj ):
        xx = np.reshape( self.scaleDownMjj(mjj), (-1,1) )
        return self.model.predict( xx )
        
        
    def scaleDownMjj( self, x ):
        return (x-2*self.Mjj_selection)/self.Mjj_scaling
    
    
    def select_events( self, mjj, loss ):
        cut = self.predict( mjj )
        return loss > cut.flatten()
    
    
    def select_events_regression_cut( self, mjj, loss, max_accepted_mjj ):
        cut = self.predict( np.minimum(mjj,max_accepted_mjj) ) # cut values at max qcd accepted mjj
        return loss > cut.flatten()

    
    def save( self, path ):
        self.model.save( path )
        
    def load( self, path ):
        self.model = load_model( path )