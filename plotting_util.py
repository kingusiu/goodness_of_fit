import matplotlib.colors as colors
from matplotlib.colors import LogNorm
import h5py, os, sys, glob
import numpy as np
import matplotlib.pyplot as plt

def plot_hist( data, bins=100, xlabel='x', ylabel='num frac', title='histogram', plot_name='', fig_dir=None, legend=[], ylogscale=True, normed=True ):
    fig = plt.figure( figsize=(7,5) )
    counts, edges = plot_hist_on_axis( plt.gca(), data, bins, xlabel, ylabel, title, legend, ylogscale, normed )
    plt.xticks(fontsize=14)
    if legend:
        plt.legend(loc='best',prop={'size': 11})
    plt.tight_layout()
    if fig_dir:
        fig.savefig(os.path.join( fig_dir, plot_name + '_hist.png'))
    plt.show()
    plt.close()
    return [counts,edges]


def plot_hist_on_axis( ax, data, bins, xlabel, ylabel, title, legend=[], ylogscale=True, normed=True ):
    alpha = 1.0
    histtype = 'step'
    if ylogscale:
        ax.set_yscale('log', nonposy='clip')
        #ax.set_ylim(1,None)
    counts, edges, _ = ax.hist( data, bins=bins, normed=normed, alpha=alpha, histtype='step', linewidth=1.2, label=legend )
    ax.set_ylabel( ylabel )
    ax.set_xlabel( xlabel )
    ax.set_title( title )
    #ax.tick_params(axis='both', which='minor', labelsize=5)
    #ax.set_ylim(bottom=1e-7)
    return [counts, edges]
    

def plot_hist_2d( x, y, xlabel='x', ylabel='y', title='2d hist', plot_name='plot', fig_dir=None):
    fig = plt.figure()
    ax = plt.gca()
    im = plot_hist_2d_on_axis( ax, x, y, xlabel, ylabel, title )
    fig.colorbar(im[3])
    plt.tight_layout()
    if fig_dir:
        plt.savefig(os.path.join(fig_dir,plot_name+'_hist2d.png'))
    plt.show()
    #plt.close()
    return ax
    
    
def plot_hist_2d_on_axis( ax, x, y, xlabel, ylabel, title ):
    im = ax.hist2d(x, y, bins=100, norm=colors.LogNorm())
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return im

    
def plot_step( x, ys, labels='dat', xlabel='x', title='title', ylim=None, ylog=True):
    plt.figure()
    for y, label in zip(ys,labels):
        plt.step(x,y,label=label)
    plt.legend()
    if ylog:
        plt.yscale('log')
    plt.ylim(ylim)
    plt.xlabel(xlabel)
    plt.title(title)
    #plt.savefig(os.path.join(fig_dir,'qcd_signalreg_vs_GtoTTbarBroad_before_vae_cut.png'))
    plt.show()
    plt.close()
    
    
def plot_counting_hist( data, bins=7, xlabel='x', ylabel='count', title='hist', plot_name='plot', fig_dir=None ):
    """ plot histogram with bin count values displayed above bins """
    plt.figure()
    bin_counts, bin_edges, _ = plt.hist( data, bins=bins, alpha=0.7, facecolor='g' )
    for i, n, in zip(bin_edges,bin_counts):
        if n != 0: plt.text(i*1.05, n*2, str(int(n)), va='center', fontsize=12)
    plt.yscale('log')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if fig_dir:
        plt.savefig(os.path.join(fig_dir,plot_name+'_count_hist.png'))
    plt.show()
    plt.close()
    
    
def plot_boxplot( data, title='boxplot', plot_name='boxplot', fig_dir=None, outlier=True ):
    plt.figure()
    if outlier: plt.boxplot(data)
    else: plt.boxplot(data,0,'')
    plt.title(title)
    if fig_dir:
        plt.savefig(os.path.join(fig_dir,plot_name+'_boxplot.png'))
    plt.show()
    plt.close()
