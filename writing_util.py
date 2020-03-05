import h5py
import numpy as np


def write_data_to_file( datasets, labels, file_path ):
    f = h5py.File(file_path, 'w')
    for dat, label in zip(datasets,labels):
        f.create_dataset(label,data=dat, compression='gzip')
    f.close()


def write_results_recarray_to_file( results, file_path ):
    f = h5py.File(file_path, 'w')
    f.create_dataset('results', data=results,  compression='gzip')
    f.create_dataset('labels', data=np.array(results.dtype.names, dtype='S')) # encode in bytes as h5py can't handle unicode
    f.close()
    
