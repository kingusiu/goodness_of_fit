from abc import ABCMeta, abstractmethod
import numpy as np
import sklearn.ensemble as scikit
import joblib as jl

import quantile_regression_dnn as qr
import flat_cut as fc


class Selector( ):
    
    __metaclass__ = ABCMeta
   
    def __init__( self, quantile ):
        self.quantile = quantile
        
    def save( self, path ):
        self.model.save( path )
        
    @abstractmethod
    def load( self, path ):
        pass
    
    @abstractmethod
    def fit( self, *args ):
        pass
    
    @abstractmethod
    def select_events( self, *args ):
        pass
    
    @abstractmethod
    def title( self ):
        pass
    

class QuantileRegressionSelector( Selector ):
    
    def fit( self, *args ):
        x, y = args
        self.model = qr.Quantile_Regression( self.quantile )
        self.model.fit( x, y )
        
    def select_events( self, *args ):
        x, y = args
        return self.model.select_events( x, y )
    
    def load( self, path ):
        self.model = qr.Quantile_Regression( self.quantile )
        self.model.load( path )
        
    def title( self ):
        return 'QR full'

    
class QuantileRegressionOverflowBinSelector( Selector ):
   
    def fit( self, *args ):
        x, y = args
        self.model = qr.Quantile_Regression_Overflow_Bin( self.quantile )
        self.model.fit( x, y )
        
    def select_events( self, *args ):
        x, y = args
        return self.model.select_events( x, y )
    
    def load( self, path ):
        self.model = qr.Quantile_Regression_Overflow_Bin( self.quantile )
        self.model.load( path )

    def title( self ):
        return 'QR overflow'

    
class FlatCutSelector( Selector ):
    
    def fit( self, *args ):
        _, y = args
        self.cut = np.percentile( y, (1.-self.quantile)*100 )
        
    def select_events( self, *args ):
        _, y = args
        return y > self.cut
    
    def save( self, path ):
        print('save not implemented for flat cut')
        # todo: write cut value to file? (overkill)
        
    def load( self, path ):
        print('load not implemented for flat cut')
        # todo: read cut value from file?
        
    def title( self ):
        return 'Flat cut'

        
class GradientBoostRegresssor( Selector ):
    
    def fit( self, *args ):
        x, y = args
        x = x.reshape(-1,1)
        self.model = scikit.GradientBoostingRegressor( loss='quantile', alpha=1-self.quantile, learning_rate=.01, max_depth=2, verbose=2 )
        self.model.fit( x, y )
        
    def select_events(self, *args ):
        x, y = args
        x = x.reshape(-1,1)
        cut = self.model.predict( x )
        return y > cut.flatten()
    
    def save( self, path ):
        jl.dump( self.model, path )
        
    def load( self, path ):
        self.model = jl.load( path )
        
    def title( self ):
        return 'GBR'

    
    #### utility functions ####

def split_by_selection( boosted_sample ):
    accepted = boosted_sample[ boosted_sample['sel'] ]
    rejected = boosted_sample[ ~boosted_sample['sel'] ]
    return ( accepted, rejected )
    
def get_bin_counts_total_acc_rej( boosted_sample, bin_edges ):
    accepted, rejected = split_by_selection( boosted_sample )
    tot_count, _ = np.histogram( boosted_sample['mJJ'], bins=bin_edges )
    acc_count, _ = np.histogram( accepted['mJJ'], bins=bin_edges )
    rej_count, _ = np.histogram( rejected['mJJ'], bins=bin_edges ) 
    return [tot_count, acc_count, rej_count]    
