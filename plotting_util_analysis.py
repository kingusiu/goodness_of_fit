import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from matplotlib.colors import LogNorm

import parameter as pa
import plotting_util as pu

import ROOT as rt
rt.gErrorIgnoreLevel = rt.kError
rt.PyConfig.IgnoreCommandLineOptions = True
rt.gROOT.SetBatch()

from histo_utilities import create_TH2D, create_TH1D, create_Canvas, make_effiency_plot, rootTH1_to_np
from cebefo_style import cebefo_style
cebefo_style()


def plot_qr_2d_hist( qcd_data, loss, model, quantile, strategy, max_acc_mjj=None, regr_cut=True, plot_name='qr_2d_hist', fig_dir=None ):
    plt.figure(figsize=(8, 8))
    x_min = pa.Mjj_selection*0.8
    x_max = 7000. #np.percentile(x, 99.99)
    plt.hist2d(qcd_data['mJJ'], loss,
           range=((x_min , x_max), (np.min(loss), np.percentile(loss, 1e2*(1-1e-4)))), 
           norm=LogNorm(), bins=100, label='signal data')

    xs = np.arange(pa.Mjj_selection, x_max, 0.001*(x_max-pa.Mjj_selection))
    plt.plot(xs, model.predict( xs ) , '-', color='m', lw=2.5, label='QR selection')
    if regr_cut:
        plt.plot(xs, model.predict(np.minimum(xs,max_acc_mjj)) , '-', color='purple', lw=3, label='QR selection cut')
    
    plt.ylabel(strategy.title_str)
    plt.xlabel('$M_{jj}$ [GeV]')
    plt.title('qcd signal region '+ quantile.title_str +' QR training data')
    plt.colorbar()
    plt.legend(loc='best')
    plt.draw()
    if fig_dir:
        fig.savefig(os.path.join( fig_dir, plot_name + '.png'))
    #plt.savefig(os.path.join(fig_dir,'qcd_selection_training_hist2d.png'))
    
def plotMassSpectrum(mJJ_pass, mJJ_rej, binning, SM_eff, title='', fig_dir=None):
    
    h_a = create_TH1D(mJJ_pass, name='h_acc', title='Accepted', binning=binning, opt='overflow' )
    bin_edges = [h_a.GetXaxis().GetBinLowEdge(i) for i in range(1,h_a.GetNbinsX()+2)]
    h_a.SetLineColor(2)
    h_a.SetStats(0)
    h_a.Sumw2()
    
    h_r = create_TH1D(mJJ_rej, name='h_rej', title='Rejected', axis_title=['M_{jj} [GeV]', 'Events'], binning=binning,
                      opt='overflow' )
    bin_edges = [h_a.GetXaxis().GetBinLowEdge(i) for i in range(1,h_a.GetNbinsX()+2)]

    h_r.GetYaxis().SetRangeUser(0.5, 1.2*h_r.GetMaximum())
    h_r.SetStats(0)
    h_r.Sumw2()

    c = make_effiency_plot([h_r, h_a], ratio_bounds=[1e-4, 0.2], draw_opt = 'E', title=title)

    c.pad1.SetLogy()
    c.pad2.SetLogy()

    c.pad2.cd()
    c.ln = rt.TLine(h_r.GetXaxis().GetXmin(), SM_eff, h_r.GetXaxis().GetXmax(), SM_eff)
    c.ln.SetLineWidth(2)
    c.ln.SetLineStyle(7)
    c.ln.SetLineColor(8)
    c.ln.DrawLine(h_r.GetXaxis().GetXmin(), SM_eff, h_r.GetXaxis().GetXmax(), SM_eff)

    c.Draw()

    return c


def plotMassSpectrumCombine( qcd_acc, qcd_rej, bin_edges, y_max=2 ):
    
    n_bins = len(bin_edges)-1
    max_bin = bin_edges[-1]
    min_bin = bin_edges[0]
    
    # prepare histograms and scale
    data_hist_acc = rt.TH1D('data_obs_acc','data_obs_acc', n_bins, min_bin, max_bin)
    data_hist_rej = rt.TH1D('data_obs_rej','data_obs_rej', n_bins, min_bin, max_bin)

    for i, b in enumerate(qcd_acc):
        data_hist_acc.SetBinContent(i+1, b)
    for i, b in enumerate(qcd_rej):
        data_hist_rej.SetBinContent(i+1, b)
    

    # plot background, signal, data
    c = rt.TCanvas('c','c',600,200)
    
    c.cd()
    tline = rt.TLine(min_bin, 1, max_bin, 1)
    tline.SetLineWidth(2)
    tline.SetLineColor(rt.kGreen)
    tline.Draw()
    data_hist_acc.Sumw2()
    data_hist_ratio = data_hist_acc.Clone('data_hist_ratio')
    data_hist_rej.Sumw2()
    data_hist_ratio.Divide(data_hist_rej)
    data_hist_ratio.Scale(data_hist_rej.Integral()/data_hist_acc.Integral())
    data_hist_ratio.SetLineColor(rt.kRed)
    data_hist_ratio.SetLineWidth(3)
    data_hist_ratio.Draw('pez')
    data_hist_ratio.SetMaximum(y_max)
    data_hist_ratio.SetMinimum(0)
    data_hist_ratio.Draw('pezsame')

    c.Draw()
    return [c, data_hist_ratio, tline ] 


def plotMassSpectrumCombineLogscale( qcd_acc, qcd_rej, bin_edges ):
    
    n_bins = len(bin_edges)-1
    max_bin = bin_edges[-1]
    min_bin = bin_edges[0]
    
    # prepare histograms and scale
    data_hist_acc = rt.TH1D('data_obs_acc','data_obs_acc', n_bins, min_bin, max_bin)
    data_hist_rej = rt.TH1D('data_obs_rej','data_obs_rej', n_bins, min_bin, max_bin)

    for i, b in enumerate(qcd_acc):
        data_hist_acc.SetBinContent(i+1, b)
    for i, b in enumerate(qcd_rej):
        data_hist_rej.SetBinContent(i+1, b)
    

    # plot background, signal, data
    c = rt.TCanvas('c','c',600,200)

    c.cd()
    c.SetLogy()
    tline = rt.TLine(min_bin, 1, max_bin, 1)
    tline.SetLineColor(rt.kGreen)
    tline.SetLineWidth(2)
    tline.Draw()
    data_hist_acc.Sumw2()
    data_hist_ratio = data_hist_acc.Clone('data_hist_ratio')
    data_hist_rej.Sumw2()
    data_hist_ratio.Divide(data_hist_rej)
    data_hist_ratio.Scale(data_hist_rej.Integral()/data_hist_acc.Integral())
    data_hist_ratio.SetLineColor(rt.kRed)
    data_hist_ratio.SetLineWidth(3)
    data_hist_ratio.Draw('pez')
    data_hist_ratio.SetMaximum(15)
    data_hist_ratio.SetMinimum(0.01)
    data_hist_ratio.Draw('pezsame')

    c.Draw()
    return [c, data_hist_ratio, tline ] 
   
def test_hist_draw():
    c = rt.TCanvas('c','c',600,600)
    h = rt.TH1F("gauss","Example histogram",100,-4,4)
    h.FillRandom("gaus")
    h.Draw()
    c.Draw()
    return c
    

def plot_accepted_vs_rejected_hist(data_sample, fig_dir=None):
    accepted = data_sample['mJJ'][data_sample['sel']]
    rejected = data_sample['mJJ'][~data_sample['sel']]
    xx = [data_sample['mJJ'], accepted, rejected]
    [h_t, h_a, h_r], _ = \
        pu.plot_hist( xx, xlabel='M_jj', bins=100, title='event selection ' + data_sample.title(), fig_dir=fig_dir, plot_name=data_sample.plot_name()+'_event_selection', legend=['total','accepted','rejected'], normed=False)
