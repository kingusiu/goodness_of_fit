
input_dir_new_data = '/eos/user/k/kiwoznia/data/VAE_data/march_2020_data/input/events/'
input_dir_old_data = '/eos/user/k/kiwoznia/data/VAE_data/october_2019_data/input/events'

result_dir_new_data = '/eos/user/k/kiwoznia/data/VAE_data/VAE_check_run_new_data_training/results'
result_dir_old_data = '/eos/user/k/kiwoznia/data/VAE_data/VAE_check_run_old_data_training/results'


model_dict = {
                    33 : 'run_33_VAE_G_relu_z5_tsz60.0K_2020-05-23_14:05:49',
                    34 : 'run_34_VAE_G_relu_z5_tsz60.0K_2020-05-23_19:18:47',
                    35 : 'run_35_VAE_G_relu_z10_tsz60.0K_2020-05-24_03:55:46',
                    36 : 'run_36_VAE_G_relu_z10_tsz60.0K_2020-05-24_20:37:04',
                    37 : 'run_37_VAE_G_relu_z10_tsz60.0K_2020-05-25_16:44:55',
                    38 : 'run_38_VAE_G_relu_z10_tsz60.0K_2020-05-25_18:31:07',
                    39 : 'run_39_VAE_G_relu_z10_tsz60.0K_2020-05-25_20:23:22'
                    }

sample_loc = { #'qcdSide': 'qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND',
               'qcdSig': 'qcd_sqrtshatTeV_13TeV_PU40_mjj_cut_concat_200K.h5',
               'GtoWW15na': 'RSGraviton_WW_NARROW_13TeV_PU40_1.5TeV_mjj_cut_concat_200K.h5',
               #'GtoWW20na': 'RSGraviton_WW_NARROW_13TeV_PU40_2.0TeV',
               'GtoWW25na': 'RSGraviton_WW_NARROW_13TeV_PU40_2.5TeV_mjj_cut_concat_200K.h5',
               'GtoWW30na': 'RSGraviton_WW_NARROW_13TeV_PU40_3.0TeV_mjj_cut_concat.h5',
               'GtoWW35na': 'RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV_mjj_cut_concat_200K.h5',
               #'GtoWW40na': 'RSGraviton_WW_NARROW_13TeV_PU40_4.0TeV',
               'GtoWW45na': 'RSGraviton_WW_NARROW_13TeV_PU40_4.5TeV_mjj_cut_concat_200K.h5',
               'GtoWW15br': 'RSGraviton_WW_BROAD_13TeV_PU40_1.5TeV_mjj_cut_concat_200K.h5',
               #'GtoWW20br': 'RSGraviton_WW_BROAD_13TeV_PU40_2.0TeV',
               'GtoWW25br': 'RSGraviton_WW_BROAD_13TeV_PU40_2.5TeV_mjj_cut_concat_200K.h5',
               #'GtoWW30br': 'RSGraviton_WW_BROAD_13TeV_PU40_3.0TeV',
               'GtoWW35br': 'RSGraviton_WW_BROAD_13TeV_PU40_3.5TeV_mjj_cut_concat_200K.h5',
               #'GtoWW40br': 'RSGraviton_WW_BROAD_13TeV_PU40_4.0TeV',
               'GtoWW45br': 'RSGraviton_WW_BROAD_13TeV_PU40_4.5TeV_mjj_cut_concat_200K.h5',
               #'AtoHZ': 'AtoHZ_to_ZZZ_13TeV_PU40',
               'GtoTTbr_old' : 'RSGraviton_tt_BROAD_13TeV_PU40_concat.h5',
               'GtoTTna_old' : 'RSGraviton_tt_NARROW_13TeV_PU40_concat.h5',
               'GtoWW25na_old': 'RSGraviton_WW_NARROW_13TeV_PU40_2p5TeV_concat.h5'
             }

sample_result_loc = {
                'qcdSide_old' : 'qcd_side_old_results.h5',
                'qcdSide_new' : 'qcd_side_new_results.h5',
                'GtoTTbr_old' : 'G_to_tt_broad_old_results.h5',
                'GtoTTna_old' : 'G_to_tt_narrow_old_results.h5',
                'GtoWW25na_old' : 'G_to_WW_narrow_2p5TeV_old_results.h5',
                'GtoWW15na_new' : 'G_to_WW_narrow_1p5TeV_new_results.h5',
                'GtoWW25na_new' : 'G_to_WW_narrow_2p5TeV_new_results.h5',
                'GtoWW30na_new' : 'G_to_WW_narrow_3p0TeV_new_results.h5',
                'GtoWW45na_new' : 'G_to_WW_narrow_4p5TeV_new_results.h5',
                'GtoWW15br_new' : 'G_to_WW_broad_1p5TeV_new_results.h5',
                'GtoWW25br_new' : 'G_to_WW_broad_2p5TeV_new_results.h5'
}