import matplotlib.colors as colors
from matplotlib.colors import LogNorm
import h5py, os, sys
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from progressBar import ProgressBar
from plotting_utilities import *


maxEvts = 1e7
Mjj_selection = 1100.0

def read_in_data( file_dir ):
    pb = ProgressBar(maxEvts)

    data = None
    flist = glob.glob(file_dir + '/' + '*result.h5')
    #print(flist)
    i_file = 0
    labels = None
    for i_file, fname in enumerate(flist):
        f = h5py.File(fname, 'r')
        #print(f.keys())
        aux_evts = np.array(f.get('results'))
        aux_evts = aux_evts[aux_evts[:,0] > Mjj_selection]
        if data is None:
            labels = list(f.get('labels'))
            print('Labels:')
            print(labels)
            pb.show(0)
            data = aux_evts
        else:
            data = np.append(data, aux_evts, axis=0)

        pb.show(data.shape[0])
    

    print('\nnum files read in dir ', file_dir, ': ', i_file+1)
    return data


base_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/VAE_results/' #'/afs/cern.ch/work/k/kiwoznia/vae_results' # /results_before_max_pixel

sample_loc = {
              'GtoWW1': base_dir + '/RSGraviton_WW_NARROW_13TeV_PU40_1.5TeV',
              'GtoWW2': base_dir + '/RSGraviton_WW_NARROW_13TeV_PU40_2.5TeV',
              'GtoWW3': base_dir + '/RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV',
              'GtoWW4': base_dir + '/RSGraviton_WW_NARROW_13TeV_PU40_4.5TeV',
              'AtoHZ': base_dir + '/AtoHZ_to_ZZZ_13TeV_PU40/',
              'GtoTTBroad': base_dir + '/RSGraviton_tt_BROAD_13TeV_PU40',
              'GtoTTNarr': base_dir + '/RSGraviton_tt_NARROW_13TeV_PU40'
             }

sample_label = {
                'GtoWW1':r'$G_{RS}(1.5 TeV)\to WW$',
                'GtoWW2':r'$G_{RS}(2.5 TeV)\to WW$',
                'GtoWW3':r'$G_{RS}(3.5 TeV)\to WW$',
                'GtoWW4':r'$G_{RS}(4.5 TeV)\to WW$',
                'AtoHZ':r'$A \to HZ \to ZZZ$',
                'GtoTTNarr':r'$G_{RS} \to tt$',
                'GtoTTBroad':r'$G_{RS} \to tt \,\, broad$',
               }

# read in data
masses = []
for n, file_dir in sample_loc.items():
    print(n)
    sample = read_in_data( file_dir )
    masses.append(sample[:,0])


plot_hist(masses,'mJJ', 'frac evts','Dijet mass','signal_mass_dist', list(sample_label.values()) )

