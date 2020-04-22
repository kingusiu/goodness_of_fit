import writing_util as wu

""" module containing wrapper for a data sample """

class DataSample( ):
    
    def __init__( self, name, data ):
        self.name = name
        self.data = data # assuming data passed as dataframe
        
    def __getitem__( self, key ):
        #""" return column as numpy(!) values """
        return self.data[key]#.values
    
    def __len__( self ):
        return len(self.data)
        
    def add_feature( self, label, values ):
        self.data[ label ] = values
        
    def dump( self, path ):
        wu.write_results_array_to_file( self.data.to_numpy(), list(self.data.columns), path )
        
