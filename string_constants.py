#!/usr/bin/env python
# coding: utf-8

# # string constants data sets

import os

input_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly'
result_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/VAE_results/pt_normalized/training_without_pt_cut'
concat_result_dir = os.path.join(result_dir,'concatenated_results')
concat_result_suffix = '_mjj_cut_result_concat.h5'

sample_loc = { 'qcdSide': 'qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND',
               'qcdSig': 'qcd_sqrtshatTeV_13TeV_PU40',
               'qcdSigBis': 'qcd_sqrtshatTeV_13TeV_PU40_BIS',
               'qcdSigAll': 'qcd_sqrtshatTeV_13TeV_PU40_ALL', # qcdSig + qcdSigBis
               'qcdSigExt':'qcd_sqrtshatTeV_13TeV_PU40_EXT',
               'qcdSigExt2': 'qcd_sqrtshatTeV_13TeV_PU40_EXT2',
               'qcdSigExt3': 'qcd_sqrtshatTeV_13TeV_PU40_EXT3',
               'qcdSigExt4': 'qcd_sqrtshatTeV_13TeV_PU40_EXT4',
               'qcdSigExt5': 'qcd_sqrtshatTeV_13TeV_PU40_EXT5',
               'GtoWW15na': 'RSGraviton_WW_NARROW_13TeV_PU40_1.5TeV',
               'GtoWW20na': 'RSGraviton_WW_NARROW_13TeV_PU40_2.0TeV',
               'GtoWW25na': 'RSGraviton_WW_NARROW_13TeV_PU40_2.5TeV',
               'GtoWW30na': 'RSGraviton_WW_NARROW_13TeV_PU40_3.0TeV',
               'GtoWW35na': 'RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV',
               'GtoWW40na': 'RSGraviton_WW_NARROW_13TeV_PU40_4.0TeV',
               'GtoWW45na': 'RSGraviton_WW_NARROW_13TeV_PU40_4.5TeV',
               'GtoWW15br': 'RSGraviton_WW_BROAD_13TeV_PU40_1.5TeV',
               'GtoWW20br': 'RSGraviton_WW_BROAD_13TeV_PU40_2.0TeV',
               'GtoWW25br': 'RSGraviton_WW_BROAD_13TeV_PU40_2.5TeV',
               'GtoWW30br': 'RSGraviton_WW_BROAD_13TeV_PU40_3.0TeV',
               'GtoWW35br': 'RSGraviton_WW_BROAD_13TeV_PU40_3.5TeV',
               'GtoWW40br': 'RSGraviton_WW_BROAD_13TeV_PU40_4.0TeV',
               'GtoWW45br': 'RSGraviton_WW_BROAD_13TeV_PU40_4.5TeV',
               'AtoHZ': 'AtoHZ_to_ZZZ_13TeV_PU40',
               'GtoTTBroad': 'RSGraviton_tt_BROAD_13TeV_PU40',
               'GtoTTNarr': 'RSGraviton_tt_NARROW_13TeV_PU40'
             }


sample_label = {'qcdSide' : r'QCD side',
                'qcdSig':r'QCD signal',
                 'qcdSigBis': 'QCD signal bis',
             'qcdSigExt':r'QCD signal ext',
             'qcdSigExt2':r'QCD signal ext2',
             'qcdSigExt3':r'QCD signal ext3',
             'qcdSigExt4':r'QCD signal ext4',
             'qcdSigExt5':r'QCD signal ext5',
             'qcdSigAll': r'QCD signal all',
             'GtoWW15na':r'$G(1.5 TeV)\to WW$ narrow',
             'GtoWW20na':r'$G(2.0 TeV)\to WW$ narrow',
             'GtoWW25na':r'$G(2.5 TeV)\to WW$ narrow',
             'GtoWW30na':r'$G(3.0 TeV)\to WW$ narrow',
             'GtoWW35na':r'$G(3.5 TeV)\to WW$ narrow',
             'GtoWW40na':r'$G(4.0 TeV)\to WW$ narrow',
             'GtoWW45na':r'$G(4.5 TeV)\to WW$ narrow',
             'GtoWW15br':r'$G(1.5 TeV)\to WW$ broad',
             'GtoWW20br':r'$G(2.0 TeV)\to WW$ broad',
             'GtoWW25br':r'$G(2.5 TeV)\to WW$ broad',
             'GtoWW30br':r'$G(3.0 TeV)\to WW$ broad',
             'GtoWW35br':r'$G(3.5 TeV)\to WW$ broad',
             'GtoWW40br':r'$G(4.0 TeV)\to WW$ broad',
             'GtoWW45br':r'$G(4.5 TeV)\to WW$ broad',
             'AtoHZ':r'$A \to HZ \to ZZZ$',
             'GtoTTBroad':r'$G \to TT broad$',
             'GtoTTNarr':r'$G \to TT narrow$'
            }

plt_name = {'qcdSide' : r'qcd_side',
             'qcdSig':'qcd_signal',
            'qcdSigBis': 'QCD_signal_bis',
             'qcdSigExt': 'qcd_signal_ext',
             'qcdSigExt2': 'qcd_signal_ext2',
             'qcdSigExt3': 'qcd_signal_ext3',
             'qcdSigExt4': 'qcd_signal_ext4',
             'qcdSigExt5': 'qcd_signal_ext5',
             'qcdSigAll': 'QCD_signal_all',
             'GtoWW15na':'G_1.5_WW_na',
             'GtoWW20na':'G_2.0_WW_na',
             'GtoWW25na':'G_2.5_VWW_na',
             'GtoWW30na':'G_3.0_WW_na',
             'GtoWW35na':'G_3.5_WW_na',
             'GtoWW40na':'G_4.0_WW_na',
             'GtoWW45na':'G_4.5_WW_na',
             'GtoWW15br':'G_1.5_WW_br',
             'GtoWW20br':'G_2.0_WW_br',
             'GtoWW25br':'G_2.5_WW_br',
             'GtoWW30br':'G_3.0_WW_br',
             'GtoWW35br':'G_3.5_WW_br',
             'GtoWW40br':'G_4.0_WW_br',
             'GtoWW45br':'G_4.5_WW_br',
             'AtoHZ': 'AtoHZtoZZZ',
             'GtoTTBroad': 'GtoTTbroad',
             'GtoTTNarr': 'GtoTTnarrow'
            }

plt_dir_name = plt_name


color = {
            'GtoWW15na':'blue',
            'GtoWW20na':'navy',
            'GtoWW25na':'deepskyblue',
            'GtoWW30na':'dodgerblue',
            'GtoWW35na':'darkblue',
            'GtoWW40na':'royalblue',
            'GtoWW45na':'mediumblue',
            'GtoWW15br':'darkred',
            'GtoWW20br':'firebrick',
            'GtoWW25br':'red',
            'GtoWW30br':'crimson',
            'GtoWW35br':'orangered',
            'GtoWW40br':'tomato',
            'GtoWW45br':'maroon',
            #'AtoHZ':r'$A \to HZ \to ZZZ$',
            #'GtoTTBroad':r'$G \to TT broad$',
            #'GtoTTNarr':r'$G \to TT narrow$'
         }

