""" module defining utility functions for manipulating, pre- and post-processing data-samples """

def split_dataset_train_test( data, frac ):
    
    """ shuffles and splits dataset into training-set and testing-set accorinding to fraction frac """
    
    N = data.shape[0]
    shuffled = data.sample(frac=1.).reset_index(drop=True) # shuffle original data
    first = shuffled[:int(N*frac)].reset_index(drop=True)
    second = shuffled[int(N*frac):].reset_index(drop=True)
    
    return [first,second]

