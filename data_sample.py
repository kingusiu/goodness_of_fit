import writing_util as wu
import reading_util as ru
import string_constants as sc

""" module containing wrapper for a data sample """

class DataSample( ):
    
    def __init__( self, name, data ):
        self.name = name
        self.data = data # assuming data passed as dataframe
        
    def __getitem__( self, key ):
        return self.data[key]#.values
    
    def __len__( self ):
        return len(self.data)
    
    def features( self ):
        return list( self.data.columns )
        
    def add_feature( self, label, values ):
        self.data[ label ] = values
        
    def accepted( self, feature=None ):
        if 'sel' not in self.data:
            print('selection not available for this data sample')
            return
        return self.data[self.data['sel']][feature] if feature else self.data[self.data['sel']]
        
    def rejected( self, feature=None ):
        if 'sel' not in self.data:
            print('selection not performed for this data sample')
            return
        return self.data[~self.data['sel']][feature] if feature else self.data[~self.data['sel']]
    
    def describe( self, feature ):
        print('mean = {0:.2f}, min = {1:.2f}, max = {2:.2f}'.format(self.data[feature].mean(),self.data[feature].min(), self.data[feature].max()))
    
    def dump( self, path ):
        dump_data = self.data
        if 'sel' in self.data: # convert selection column to int for writing
            dump_data = self.data.copy()
            dump_data['sel'] = dump_data['sel'].astype(int)
        wu.write_results_array_to_file( dump_data.values, list(dump_data.columns), path )
        
    def title( self ):
        return sc.sample_label[self.name]
    
    def plot_name( self ):
        return sc.plt_name[self.name]
        

def read_datasample_from_file( sample_name, input_path ):
    df = ru.read_results_to_dataframe( input_path )
    if 'sel' in df: # convert selection column to bool
        df['sel'] = df['sel'].astype(bool)
    return DataSample( sample_name, df )


def read_datasample_from_input_file( sample_name, input_path ):
    df = ru.read_dijet_features_to_dataframe( input_path )
    return DataSample( sample_name, df )
