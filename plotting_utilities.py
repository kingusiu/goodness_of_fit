import matplotlib.colors as colors
from matplotlib.colors import LogNorm
import h5py, os, sys, glob
import numpy as np
import matplotlib.pyplot as plt

def plot_hist( data, xlabel, ylabel, title, plotname='', legend=[], ylogscale=True ):
    fig = plt.figure( )
    plot_hist_on_axis( plt.gca(), data, xlabel, ylabel, title, legend, ylogscale )
    if legend:
        plt.legend()
    plt.tight_layout()
    fig.savefig('fig/' + plotname + '_hist.png')
    plt.show()
    plt.close()


def plot_hist_on_axis( ax, data, xlabel, ylabel, title, legend=[], ylogscale=True ):
    bin_num = 70
    alpha = 1.0
    histtype = 'step'
    if ylogscale:
        ax.set_yscale('log', nonposy='clip')
    for i, dat in enumerate(data):
        ax.hist( dat, bins=bin_num, normed=True, alpha=alpha, histtype=histtype, label=legend[i] )
    ax.set_ylabel( ylabel )
    ax.set_xlabel( xlabel )
    ax.set_title( title, fontsize=10 )
    ax.tick_params(axis='both', which='minor', labelsize=8)
    #ax.set_ylim(bottom=1e-7)
