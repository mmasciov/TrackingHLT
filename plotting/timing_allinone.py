from ROOT import *
import os,sys

gStyle.SetOptStat(0)

f0=TFile.Open("DQM_timeHarvest_genericCPE_irradiationBiasTrue_afterPR.root")
f1=TFile.Open("DQM_timeHarvest_genericCPE_irradiationBiasTrue_onDemandFalse_afterPR.root")

h0=f0.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v12/module_time_real_total")
h1=f1.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v12/module_time_real_total")

h0.SetTitle("")
h1.SetTitle("")

h0.SetLineColor(2)
h0.SetMarkerColor(2)
h1.SetLineColor(4)
h1.SetMarkerColor(4)

h0.GetXaxis().SetLabelSize(0.02)
h0.GetXaxis().SetLabelOffset(0.01)
h0.GetXaxis().SetNdivisions(-573)

ymax=1.75*max(h0.GetMaximum(),h1.GetMaximum())
h0.GetYaxis().SetRangeUser(0,ymax)
h1.GetYaxis().SetRangeUser(0,ymax)

hr=h0.Clone("h0_clone")
h1r=h1.Clone("h1_clone")

hr.Divide(h1r)

leg = TLegend(0.67, 0.7, 0.87, 0.87,"#splitline{Module-per-module time}{t#bar{t} MC (2023) with PU}")
leg.SetLineColor(0)
leg.SetFillColor(0)
leg.AddEntry(h0, "Generic CPE w/ correction", "l")
leg.AddEntry(h1, "Generic CPE (onDemand=False) w/ correction", "l")

can=TCanvas("can","",1800,1200)
can.cd()
gPad.SetBottomMargin(0.35)
gPad.SetTickx()
gPad.SetTicky()
#gPad.SetLogy()

h0.Draw()
h1.Draw("same")

leg.Draw("same")

can.Update()

can.Print("timing_permodule.pdf")
can.Print("timing_permodule.png")

can.Clear()
can.cd()
gPad.SetBottomMargin(0.35)
gPad.SetTickx()
gPad.SetTicky()
#gPad.SetLogy()

h0.GetXaxis().SetRangeUser(19,82)
h1.GetXaxis().SetRangeUser(19,82)
h0.GetYaxis().SetTitle("Processing time [ms]")

print h0.GetNbinsX()

h0.Draw()
h1.Draw("same")

leg.Draw("same")

can.Update()

can.Print("timing_permodule.pdf")
can.Print("timing_permodule.png")

can.Clear()

ymin=0
ymax=1.2
hr.GetYaxis().SetRangeUser(ymin,ymax)
hr.GetYaxis().SetTitle("Generic CPE w/ correction; onDemand True/False")

#line=TLine(0,1.0,hr.GetNbinsX(),1.0)
line=TLine(19,1.0,82,1.0)
line.SetLineColor(1)

can.cd()
gPad.SetBottomMargin(0.35)
gPad.SetTickx()
gPad.SetTicky()
gPad.SetLogy(0)

hr.GetXaxis().SetRangeUser(19,82)
hr.Draw()
line.Draw("same")

can.Print("timing_permodule_ratio.pdf")
can.Print("timing_permodule_ratio.png")
