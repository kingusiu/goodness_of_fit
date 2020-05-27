import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as skl


def plot_bg_vs_sig_distribution( data, bins=100, xlabel='x', ylabel='counts', title='bg vs sig distribution', legend=[], normed=True, ylogscale=True, fig_dir=None, plot_name='bg_vs_sig_dist', legend_loc='best'):
    
    fig = plt.figure( figsize=(6,4) )
    alpha = 0.2
    histtype = 'stepfilled'
    if ylogscale:
        plt.yscale('log')
    
    for i, dat in enumerate(data):
        if i > 0:
            histtype = 'step'
            alpha = 1.0
        plt.hist( dat, bins=bins, normed=normed, alpha=alpha, histtype=histtype, label=legend[i] )
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend(loc=legend_loc)
    plt.tight_layout()
    plt.draw()
    if fig_dir:
        fig.savefig(os.path.join( fig_dir, plot_name + '.png'))
        
        
def get_label_and_score_arrays( neg_class_losses, pos_class_losses ):
    
    labels = []
    losses = []
    
    for neg_loss, pos_loss in zip(neg_class_losses, pos_class_losses):
        labels.append( np.concatenate([np.zeros(len(neg_loss)),np.ones(len(pos_loss))]) )
        losses.append( np.concatenate([neg_loss,pos_loss]) )
        
    return [labels,losses]
        
        
        
def plot_roc( y_true_arr, loss_arr, legend=[], title='ROC', legend_loc=(-0.1, -0.4)):
    
    aucs = []
    plt.figure( figsize=(5,5))
    
    for y_true, loss, label in zip( y_true_arr, loss_arr, legend ):
        fpr, tpr, threshold = skl.roc_curve( y_true, loss )
        aucs.append( skl.roc_auc_score( y_true, loss ) )
        plt.loglog( fpr, tpr, label=label+ " (auc " + "{0:.3f}".format(aucs[-1]) + ")" )
        
    plt.xlim(left=0.00001)
    plt.grid()
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.legend(loc=legend_loc)
    plt.tight_layout()
    plt.title(title)
    plt.show()
    
    return aucs
