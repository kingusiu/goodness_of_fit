class Booster():
    
    
    def __init__( self, quantile, strategy, selector_T ):
        self.quantile = quantile
        self.strategy = strategy
        self.selector_T = selector_T
        
        
    def train_selector( self, training_sample ):
        
        combined_loss = self.strategy( training_sample )

        self.selector = self.selector_T( self.quantile.val )
        self.selector.fit( training_sample['mJJ'].values, combined_loss )
        
        
    def save_selector( self, path ):
        self.selector.save( path )

        
    def load_selector( self, path ):
        self.selector.load( path )

        
    def boost_sample( self, sample ):
        
        """ returns sample augmented by loss combination according to 'strategy' and a selection feature
        indicating for each event if it passed the anomaly discriminant ('sel'=True, i.e. anomalous) or failed it
        ('sel'=False, i.e. standard model) """
        
        sample.add_feature('combiLoss', self.strategy( sample ))
        selection = self.selector.select_events( sample['mJJ'].values, sample['combiLoss'].values )
        sample.add_feature('sel', selection)
        
        