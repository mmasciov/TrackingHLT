from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle

def main():
	
	canv = TCanvas("c1","c1",800,800)

	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	style = setTDRStyle()
	gStyle.SetTitleYOffset(1.45)
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	plotPad.Draw()	
	plotPad.cd()
#	plotPad.DrawFrame(0,0.2,1500,50000,";time [ms]; Events / 50 ms")
	plotPad.DrawFrame(0,0.2,2500,40000,";time [ms]; Events / 50 ms")
	plotPad.SetLogy()

	
	fIdeal = TFile("DQM_timeHarvest_genericCPE_irradiationBiasTrue_afterPR.root","OPEN")
	histIdeal = fIdeal.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v12/path time_real")
	fCPE = TFile("DQM_timeHarvest_genericCPE_irradiationBiasTrue_onDemandFalse_afterPR.root","OPEN")
	histCPE = fCPE.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v12/path time_real")
	print histIdeal.GetNbinsX(), histIdeal.GetBinLowEdge(1), histIdeal.GetBinLowEdge(histIdeal.GetNbinsX()), histIdeal.GetBinWidth(1)
	histIdeal.Rebin(10)
	histCPE.Rebin(10)

	histIdeal.Draw("samehist")
	histIdeal.SetLineColor(kRed)
	histCPE.SetLineColor(kBlue)
	histCPE.Draw("samehist")
	

	leg = TLegend(0.42, 0.61, 0.89, 0.92,"HLT PF Tracking Timing","brNDC")
	leg.SetFillColor(10)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)
	leg.SetBorderSize(1)		
	leg.AddEntry(histIdeal,"Generic CPE w/ correction %.2f ms"%histIdeal.GetMean(),"l")
	leg.AddEntry(histCPE,"Generic CPE (onDemand=False) w/ correction %.2f ms"%histCPE.GetMean(),"l")
	leg.Draw("same")
	
	latex = TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	latexCMS = TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.055)
	latexCMS.SetNDC(True)
	latexCMSExtra = TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.03)
	latexCMSExtra.SetNDC(True) 
		
	latex.DrawLatex(0.95, 0.96, "(13 TeV)")
	
#	cmsExtra = "Preliminary"
	cmsExtra = "Simulation"
	latexCMS.DrawLatex(0.19,0.88,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.81	
	else:
		yLabelPos = 0.84	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				
	
	
	canv.Print("timingIO_TTbarMC_genericCPE_wCorrection_onDTvsF.pdf")
	canv.Print("timingIO_TTbarMC_genericCPE_wCorrection_onDTvsF.png")	
	
	
main()
