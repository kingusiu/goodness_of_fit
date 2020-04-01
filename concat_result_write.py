#!/usr/bin/env python
# coding: utf-8


import os
import reading_util as ru
import writing_util as wu
import string_constants as sc


# datasets
SM_samples = ['qcdSig','qcdSigBis']
BSM_samples = ['GtoWW15na', 'GtoWW20na', 'GtoWW25na', 'GtoWW30na', 'GtoWW35na', 'GtoWW40na', 'GtoWW45na', \
              'GtoWW15br', 'GtoWW20br', 'GtoWW25br', 'GtoWW30br', 'GtoWW35br', 'GtoWW40br', 'GtoWW45br']
all_samples = SM_samples + BSM_samples


for sample in all_samples:
    
    print('\n ++++ concatenating', sample, '++++')

    # read in data
    in_path = os.path.join( sc.result_dir, sc.sample_loc[sample] )
    results, labels = ru.read_results( in_path )


    print('read',len(results),'results. writing to concat file')
    out_path = os.path.join( sc.concat_result_dir, sc.sample_loc[sample] + '_mjj_cut_result_concat.h5') 
    dataset_names = ['results','labels']
    wu.write_data_to_file( [results, labels], dataset_names, out_path )

