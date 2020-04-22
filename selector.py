from abc import ABC, abstractmethod
import numpy as np

import quantile_regression_dnn as qr
import flat_cut as fc


class Selector( ABC ):
   
    def __init__( quantile ):
        self.quantile = quantile
        
    @abstractmethod
    def fit( self, *args ):
        pass
    
    @abstractmethod
    def select_events( self, *args ):
        pass


class QuantileRegressionSelector( Selector ):
    
    def fit( self, x, y ):
        self.model = qr.Quantile_Regression( self.quantile )
        self.model.fit( x, y )
        
    def select_events( self, *args ):
        x, y = args
        return self.model.select_events( x, y )
        

class QuantileRegressionOverflowBinSelector( Selector ):
   
    def fit( self, *args ):
        x, y = args
        self.model = qr.Quantile_Regression( self.quantile )
        self.model.fit( x, y )
        # get overflow bin (max accepted mjj) for regression cut
        sel = self.model.select_events( x, y ) # get selection for qcd training set
        self.max_acc = np.max(x[sel]) # get max mjj in accepted set
        
        
    def select_events( self, *args ):
        x, y = args
        return self.model.select_events_regression_cut( x, y, self.max_acc )
    
    
class FlatCutSelector( Selector ):
    
    def fit( self, *args ):
        self.model = fc.FlatCut( self.quantile )
        self.model.fit( *args )
        
    def select_events( self, *args ):
        return self.model.select_events( *args )
    