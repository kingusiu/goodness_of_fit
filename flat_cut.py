import numpy as np

class FlatCut( ):
    
    def __init__( self, quantile ):
        self.quantile = quantile
    
    def fit( self, loss ):
        self.cut = np.percentile( loss, (1.-self.quantile)*100 )
        
    def select_events( self, loss ):
        return loss > self.cut