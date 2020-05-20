import loss_strategy_fun as lof
import selector as sel


Mjj_selection = 1100.


class Parameter( object ):
    
    def __init__(self, val, title_str, path_str):
        self.val = val
        self.title_str = title_str
        self.path_str = path_str
        
    
class Quantile( Parameter ):
    pass


class LossStrategy( Parameter ):
    
    def __call__( self, x ):
        return self.val( x )

    
class Selector_Param( Parameter ):
    
    def __call__( self, x ):
        return self.val( x )


    
loss_strategy_dict = { 's1' : LossStrategy(lof.combine_loss_l1, 'L1 > LT', 'l1_loss'),
                     's2': LossStrategy(lof.combine_loss_l2, 'L2 > LT', 'l2_loss'),
                     's3': LossStrategy(lof.combine_loss_sum, 'L1 + L2 > LT', 'suml1l2_loss'),
                     's4': LossStrategy(lof.combine_loss_max, 'L1 | L2 > LT', 'maxl1l2_loss'),
                     's5': LossStrategy(lof.combine_loss_min, 'L1 & L2 > LT', 'minl1l2_loss')
                 }


quantile_dict = {'q1': Quantile(1e-2, '1% quantile', 'qu_1pct'), 
                  'q2': Quantile(2e-2, '2% quantile', 'qu_2pct'),
                  'q5': Quantile(5e-2, '5% quantile', 'qu_5pct'),
                  'q10': Quantile(1e-1, '10% quantile', 'qu_10pct'),
                  'q25': Quantile(0.25, '25% quantile', 'qu_25pct'),
                  'q50': Quantile(0.5, '50% quantile', 'qu_50pct'),
                  'q75': Quantile(0.75, '75% quantile', 'qu_75pct'),
                  'q90': Quantile(0.9, '90% quantile', 'qu_90pct'),
                  'q99': Quantile(0.99, '99% quantile', 'qu_99pct'),
                 }

selector_dict = { 'flat' : Selector_Param( sel.FlatCutSelector, 'Flat Cut', 'flat_cut' ),
                      'qr_over' : Selector_Param( sel.QuantileRegressionOverflowBinSelector, 'QR overflow', 'QR_overflow'),
                      'qr_full' : Selector_Param( sel.QuantileRegressionSelector, 'QR full', 'QR_full'),
                      'gbr' : Selector_Param( sel.GradientBoostRegresssor, 'GBR', 'GBR' )
                    }