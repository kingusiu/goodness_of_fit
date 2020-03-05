#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import os
from reading_util import *


# In[2]:


input_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND_EXT2'
file_name = 'qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND_EXT2_1000.h5'
file = h5py.File( os.path.join( input_dir, file_name ), 'r')
print(file.keys())


# In[3]:


jet_const = np.array( file.get('jetConstituentsList') )
print('num events = ', jet_const.shape )


# In[4]:


jet_feature_names = np.array( file.get('eventFeatureNames'))
print(jet_feature_names)
particle_feature_names = np.array( file.get('particleFeatureNames') )
print( particle_feature_names )
print( len(file.get('eventFeatureNames')) )


# In[7]:


from reading_util import *
jet_const_pt1_over, jet_feat_pt1_over, jet_const_pt1_under, jet_feat_pt1_under, keys = read_dijet_events_and_features( input_dir )


# In[14]:

print('num events ptj1 > 1000: ', jet_const_pt1_over.shape[0])
print('num events ptj1 <= 1000: ', jet_const_pt1_under.shape[0])



# In[15]:


output_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/VAE_data/split_by_jet1_pt/qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND_EXT2'
output_file_name_pt1_over = 'qcd_SIDEBAND_EXT2_concat_mjj_over_1100_ptj1_over_1000_events.h5'
output_file_name_pt1_under = 'qcd_SIDEBAND_EXT2_concat_mjj_over_1100_ptj1_under_1000_events.h5'
output_file_pt_over = os.path.join(output_dir,output_file_name_pt1_over)
output_file_pt_under = os.path.join(output_dir,output_file_name_pt1_under)
output_file_pt_over = h5py.File(output_file_pt_over,'w')
output_file_pt_under = h5py.File(output_file_pt_under,'w')


# In[17]:


print(jet_feature_names)
print( particle_feature_names )



# In[19]:


output_file_pt_over.create_dataset('eventFeatureNames', data=jet_feature_names)
output_file_pt_over.create_dataset('eventFeatures', data=jet_feat_pt1_over, compression='gzip')
output_file_pt_over.create_dataset('particleFeatureNames', data=particle_feature_names)
output_file_pt_over.create_dataset('jetConstituentsList',data=jet_const_pt1_over, compression='gzip')
output_file_pt_over.close()


# In[20]:


output_file_pt_under.create_dataset('eventFeatureNames', data=jet_feature_names)
output_file_pt_under.create_dataset('eventFeatures', data=jet_feat_pt1_under, compression='gzip')
output_file_pt_under.create_dataset('particleFeatureNames', data=particle_feature_names)
output_file_pt_under.create_dataset('jetConstituentsList',data=jet_const_pt1_under, compression='gzip')
output_file_pt_under.close()
