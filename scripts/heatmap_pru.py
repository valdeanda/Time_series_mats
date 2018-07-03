#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#------------------------------
# Name:     
# Purpose:  
# 
# @uthor:   acph - dragopoot@gmail.com
#
# Created:     
# Copyright:   (c) acph 2015
# Licence:     GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
#------------------------------
""" """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import scipy.cluster.hierarchy as sch

def load_listdict(filename, sep=' ', single=False):
    """Loads a file into a python dictionary
    
    Arguments:
    - `filename`: The file name(path) the file must contain the folowing structure:
        * each line is a element of the dictionary
        * the first word is the key
        * following by a \t
        * next the elements corresponding to the value separated by 'sep'
    - `sep`: separator of the elements in the list
    - `single`: If sigle == True, the list file will be trated as a single dictionary, one key > one value. If False, the function asumes a the dictionary includes many values sep separated per key
    """
    dictionary = {}
    with open(filename, 'r') as inf:
        for line in inf:
            line = line.strip()
            line = line.split('\t')
            if line == '' : continue
            k = line[0]
            if single == True:
                v = line[1]
            else:
                v = line[1].split(' ')
            dictionary[k] = v
    return dictionary

# set params
matplotlib.rcParams['lines.linewidth'] = 0.4

# load data
data = pd.read_pickle('datamat_non0.pd')

#data scaling normaliation
data_scaling = (data.T - data.T.min())/(data.T.max() - data.T.min())
data = data_scaling.T

#######################
# Calculate distances #
#######################
## - Metagenome distances
metadist = sch.distance.pdist(data, metric='braycurtis')
metalink = sch.linkage(metadist, method='average')
metalink = metalink.clip(0, metalink.max()+1)

## - Profile distances
profdist = sch.distance.pdist(data.T, metric='braycurtis')
proflink = sch.linkage(profdist, method='average')
proflink = proflink.clip(0, proflink.max()+1)

############
# Plotting #
############
## - figure setup
xf = 6.7
yf = 8.6
fig = plt.figure(figsize=(xf, yf))
# positions
# posm = [0.05, 0.05, 0.2, 0.7]
# posm_colors = [0.25, 0.05, 0.01, 0.7]
# posp = [0.26, 0.76, 0.6, 0.2]
# posmat = [0.26, 0.05, 0.6, 0.7]
# poscbar = [0.91,0.1,0.02,0.8]

posm = [0.01, 0.01, 0.2, 0.82]
posp = [0.24, 0.84, 0.67, 0.15]
posmat = [0.24, 0.01, 0.67, 0.82]
posm_colors = [0.215, 0.01, 0.02, 0.82]
#poscbar = [0.94, 0.01, 0.02, 0.41]
poscbar = [0.92, 0.01, 0.015, 0.40]

## - Metagenome dendogram
meta_ax = fig.add_axes(posm, frameon=False)
metadend = sch.dendrogram(metalink,
                          color_threshold=0.2*max(metalink[:,2]),
                          orientation='right')
meta_ax.set_xticks([])
meta_ax.set_yticks([])

## - Profile dendogram
prof_ax = fig.add_axes(posp, frameon=False)
profdend = sch.dendrogram(proflink,
                          color_threshold=0.2*max(proflink[:,2]),
                          orientation='top')
prof_ax.set_xticks([])
prof_ax.set_yticks([])

## - Matrix
matrix_ax = fig.add_axes(posmat)
mat = data.get_values()
mmask = metadend['leaves']
pmask = profdend['leaves']
mat = mat[mmask, :]
mat = mat[:, pmask]
im = matrix_ax.matshow(mat, aspect='auto', origin='lower')
matrix_ax.set_yticks([])

# loadign and creating top pfam
def labels_names(data, namelist):
    """Plot in x label the names in list
    
    Arguments:
    - `data`: panda DataFrame
    - `namelist`: a python list of names. Must be contained in
    pandas data.columns
    """
    labels = []
    for col in data.columns:
        if col in namelist:
            labels.append(col)
        else:
            labels.append('')
    return np.array(labels)

top_pfam = pd.read_table('top_pfam_profiles.txt', index_col=0)
top_p = list(top_pfam.index)
labs = labels_names(data, top_p)
labs = labs[pmask]

plt.xticks(np.arange(len(labs)), labs, rotation=90,
           fontsize='xx-small', color='grey')

## - Colorbar
colorbar_ax = fig.add_axes(poscbar)
cb = plt.colorbar(im, cax=colorbar_ax)
cb.set_label('Normalized data', fontsize='x-small')
cb.ax.tick_params(labelsize='xx-small')

## - Color code
color_as = {'Air': 'grey',
            'Animal/plant_associated' : 'green',
            'Biofilms/microbialites': 'red',
            'Soil/sediment': 'yellow',
            'Water': 'blue'}
clas = load_listdict('clasification_environments',
                     single=True)
color_vec = [color_as[clas[i[0]]] for i in data.index]
color_vec = np.array(color_vec)
color_vec = color_vec[mmask]
#color_vec = np.random.rand(len(data))
#filler = np.zeros(len(color_vec))
#color_mat = np.vstack((color_vec, filler)).T
color_ax = fig.add_axes(posm_colors, frameon=False)
lefts = range(0, len(color_vec), 1)
height = np.ones(len(color_vec))
width = 1
metabars = color_ax.barh(lefts, height, width, color=color_vec,
                        edgecolor=color_vec)
#im_col = color_ax.matshow(color_mat, aspect='auto', origin="lower")
#color_ax.set_xlim(-0.5, 0.5)
color_ax.set_xticks([])
color_ax.set_yticks([])
color_ax.set_ylim((0, len(color_vec)))

## - show
#plt.show()
fig.savefig('heatmap_pru.png', dpi=500)


## - color legend
import matplotlib.patches as mpatches
poslegend = [0.01, 0.84, 0.23, 0.15]
legend_ax = fig.add_axes(poslegend, frameon=False)
legend_ax.set_xticks([])
legend_ax.set_yticks([])

patches = []
for name, color_ in color_as.iteritems():
    p = mpatches.Patch(color=color_, label=name)
    patches.append(p)

plt.legend(handles=patches, fancybox=True, fontsize='xx-small')


## - show
#plt.show()

fig.savefig('heatmap_pru.png', dpi=500)

## -save data
clustdata = data.iloc[mmask, pmask]
clustdata.to_csv('matdata_clust_pru.txt', sep='\t')