# std lib imports
import numpy as np
import pandas as pd
import h5py
import os
import sys
from glob import glob

# custom imports
from progressBar import ProgressBar

# constants
Mjj_cut = 1100
pt_j1_cut = 1000

# *****************************************
#    main reading functions

# result data

def read_results( input_path ):
    if os.path.isfile( input_path ):
        return read_data_from_file( input_path, 'results','labels' )
    else:
        return read_data_from_dir( input_path, 'results','labels' )
    

def read_results_to_recarray( input_path ):
    data, labels = read_results( input_path )
    return [ data_to_recarray( data, labels ), labels ]


def read_results_to_dataframe( input_path ):
    data, labels = read_results( input_path )
    return pd.DataFrame(data,columns=labels)

# input data: only dijet features

def read_dijet_features( input_path ):
    if os.path.isfile( input_path ):
        return read_data_from_file( input_path, 'eventFeatures','eventFeatureNames' )
    else:
        return read_data_from_dir( input_path, 'eventFeatures','eventFeatureNames' )
    
    
def read_dijet_features_to_recarray( input_path ):
    data, labels = read_dijet_features( input_path )
    return [ data_to_recarray( data, labels ), labels ]

# input data: particles and dijet features

def read_inputs( input_path ):
    if os.path.isfile( input_path ):
        return read_dijet_events_and_features_from_file( input_path )
    else:
        return read_dijet_events_and_features_from_dir( input_path )


# *****************************************
#    auxiliary functions

def data_to_recarray( data, labels ):
    #dt = [(s.decode("utf-8"), '<f4') for s in labels]
    dt = [(str(s), '<f4') for s in labels]
    return np.array(list(zip(*data.T)), dtype=dt)


def recarray_to_data( arr ):
    return arr.view((arr.dtype[0],len(arr.dtype.names)))
    

def read_data_from_file( file_path, *keys ):
    data = []
    with h5py.File(file_path,'r') as f:
        if not keys:
            keys = f.keys()
        for k in keys:
            data.append(np.array(f.get(k)))
    return data


def get_file_list( dir_path ):
    flist = []
    for path, _, _ in os.walk( dir_path, followlinks=True ):
        print('reading ', path)
        flist += glob(path + '/' + '*.h5')
    return flist


# reading routine
def read_data_from_dir( dir_path, datakey, labelkey ):
    print('reading', dir_path)
    maxEvts = int(1e9)
    pb = ProgressBar(maxEvts)

    data = []
    
    flist = get_file_list( dir_path )
    print('num files in dir:',len(flist))
    pb.show(0)
    
    for i_file, fname in enumerate(flist):
        try:
            results, = read_data_from_file( fname, datakey )
            results = results[results[:,0] > Mjj_cut]
            data.extend(results)
            pb.show(len(data))
        except Exception as e:
            print("\nCould not read file ", fname, ': ', repr(e))
            
    labels, = read_data_from_file( fname, labelkey )
    print('Labels:', labels)

    print('\nnum files read in dir ', dir_path, ': ', i_file+1)
    return [ np.asarray(data), labels ] 


def read_dijet_events_and_features_from_dir( dir_path ):
    print('reading', dir_path)
    maxEvts = int(1.2e6)
    pb = ProgressBar(maxEvts)

    constituents_concat = []
    features_concat = []
    
    flist = get_file_list( dir_path )
    print('num files in dir:',len(flist))
    pb.show(0)
    
    for i_file, fname in enumerate(flist):
        try:
            constituents, features = read_dijet_events_and_features_from_file( fname )
            constituents, features = filter_arrays_on_value( [constituents,features], features[:,0], Mjj_cut)
            constituents_concat.extend(constituents)
            features_concat.extend(features)
            pb.show(len(constituents_concat))
        except Exception as e:
            print("\nCould not read file ", fname, ': ', repr(e))
        if len(constituents_concat) > maxEvts :
            break
    
    particle_feature_names, = read_data_from_file( fname, 'particleFeatureNames' )
    evt_feature_names, = read_data_from_file( fname, 'eventFeatureNames' )
    
    print('\nnum files read in dir ', dir_path, ': ', i_file+1)
    return [ constituents_concat, particle_feature_names, features_concat, evt_feature_names ] 


def read_dijet_events_and_features_from_file( input_file ):
        
    f = h5py.File( input_file ,'r')

    features = np.array(f.get('eventFeatures'))
    constituents = np.array(f.get('jetConstituentsList'))

    return [constituents, features]


def filter_arrays_on_value( arrays, filter_array, filter_value ):
    idx_after_cut = filter_array > filter_value
    return [a[idx_after_cut] for a in arrays]


def read_dijet_events_and_features_pt_split( input_dir ):
        
    flist = glob( input_dir + '/' + '*.h5' )
    f = h5py.File(flist[0],'r')
    keys = f.keys()

    maxEvts = int(1e9)
    pb = ProgressBar(maxEvts)

    jet_const_pt1_over = np.empty((0,2,100,3),int) # each event = 2 jets, each 100 particles, each ( dEta, dPhi, pt )
    jet_const_pt1_under = np.empty((0,2,100,3),int)
    jet_feat_pt1_over = np.empty((0,11),int) # 11 jet features per event
    jet_feat_pt1_under = np.empty((0,11),int)

    fnum = 0
    evt_num = 0

    pb.show(evt_num)

    for fnum, fname in enumerate( flist ):
        f = h5py.File( fname, 'r' )
        aux_features = np.array(f.get('eventFeatures'))
        aux_constituents = np.array(f.get('jetConstituentsList'))
        evt_num = evt_num + aux_constituents.shape[0]
        # mass cut
        aux_features, aux_constituents = filter_arrays_on_value([aux_features,aux_constituents],aux_features[:,0], Mjj_cut)
        # pt_j1 separation
        pt_cut_passed = aux_features[:,1] > pt_j1_cut
        jet_const_pt1_over = np.append(jet_const_pt1_over,aux_constituents[pt_cut_passed],axis=0)
        jet_feat_pt1_over = np.append(jet_feat_pt1_over,aux_features[pt_cut_passed],axis=0)
        jet_const_pt1_under = np.append(jet_const_pt1_under,aux_constituents[~pt_cut_passed],axis=0)
        jet_feat_pt1_under = np.append(jet_feat_pt1_under,aux_features[~pt_cut_passed],axis=0)

        pb.show(evt_num)

        if( fnum % 100 == 0 ):
            print( evt_num, ' events read, ', jet_const_pt1_over.shape[0] + jet_const_pt1_under.shape[0], ' events passed mass cut (size = ',  (jet_const_pt1_over.nbytes + jet_const_pt1_under.nbytes) / 1000. , ' KB)')

    print( evt_num, ' events read, ', jet_const_pt1_over.shape[0] + jet_const_pt1_under.shape[0], ' events passed mass cut' )
    return [jet_const_pt1_over, jet_feat_pt1_over, jet_const_pt1_under, jet_feat_pt1_under, keys]
        
