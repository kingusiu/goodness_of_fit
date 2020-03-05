#!/usr/bin/env python
# coding: utf-8

# In[1]:


from reading_util import *
from writing_util import *
import string_constants as sc


# In[2]:


# read in data
sample = 'qcdSide'
particles, particle_feature_names, jet_features, jet_feature_names = read_dijet_events_and_features_from_dir( os.path.join( sc.input_dir, sc.sample_loc[sample] ) )


# In[4]:


out_path = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/VAE_data/qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND_mjj_cut_concat.h5' 
dataset_names = ['jetConstituentsList','particleFeatureNames','eventFeatures','eventFeatureNames']
write_data_to_file( [particles, particle_feature_names, jet_features, jet_feature_names], dataset_names, out_path )


# In[5]:


print(particles.shape)


# In[ ]:




