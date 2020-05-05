import h5py
import numpy as np


def write_data_to_file( datasets, dataset_names, file_path ):
    f = h5py.File(file_path, 'w')
    for dat, dat_name in zip(datasets,dataset_names):
        f.create_dataset(dat_name, data=dat, compression='gzip')
    f.close()

def write_results_array_to_file( results, labels, file_path ):
    f = h5py.File(file_path, 'w')
    f.create_dataset('results', data=results,  compression='gzip')
    f.create_dataset('labels', data=labels) 
    f.close()

def write_results_recarray_to_file( results, file_path ):
    # encode labels in bytes as h5py can't handle unicode
    write_results_array_to_file( results, np.array(results.dtype.names, dtype='S'), file_path)
    
    
def write_bin_counts( datasamples, bincounts, bin_edges, file_path ):
    with h5py.File( file_path, 'w' ) as file_bin_counts:
        for sample, counts in zip(datasamples,bincounts):
            file_bin_counts.create_dataset(sample, data=counts)
        file_bin_counts.create_dataset('bin_count_labels',data=['total','accepted','rejected'])
        file_bin_counts.create_dataset('bin_edges',data=bin_edges)
    
