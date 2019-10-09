from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle
import ROOT

def main():
	
	canv = TCanvas("c1","c1",800,800)
	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	style = setTDRStyle()
	ROOT.gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	plotPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)

        legendTitle = "XYZ" ### Set according to your needs
        sampleInfo = "#splitline{t#bar{t} event tracks with PU}{|#eta| < 2.5, p_{T}> 0.4 GeV}" ### Set according to your needs

	f0 = TFile("DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO_TTbar_PU25ns_102X_upgrade2018_realistic_v12-v1_1kevts.root","OPEN")
	f1 = TFile("DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root","OPEN")	
	
	trackCols = ["hltPixel_hltAssociatorByHits","hltIter2PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter2Merged_hltAssociatorByHits","hltIter1PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits"]
	trackLabels = ["pixelTracks","iter2","iter2Merged","iter1","iter0"]
	
	variables = ['efficPt','effic','effic_vs_dr','effic_vs_phi','effic_vs_pu','effic_vs_dxy','fakerate','fakeratePt','fakerate_vs_phi','duplicatesRate','duplicatesRate_Pt']

	
	for var in variables:
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMin = 0.5
		yMax = 1.5
		if 'effic' in var:
			yLabel = 'HLT Tracking Efficiency Ratio'
		elif 'fake' in var:	
			yLabel = 'Fake Rate Ratio'
		elif 'dupli' in var:	
			yLabel = 'Duplicate Rate Ratio'
			yMin=0.0
                        yMax=3.0

                if "Pt" in var:
			plotPad.SetLogx()
			plotPad.DrawFrame(0,yMin,200,yMax,";track p_{T} [GeV]; %s"%yLabel)
		elif "dr" in var:
			plotPad.SetLogx()
			plotPad.DrawFrame(0,yMin,1,yMax,";dR; %s"%yLabel)
		elif "pu" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(0,yMin,80,yMax,";PU; %s"%yLabel)
		elif "dxy" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-1,yMin,1,yMax,";dxy; %s"%yLabel)
		elif "phi" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-3,yMin,3,yMax,";#Phi; %s"%yLabel)
		else:
			plotPad.DrawFrame(-2.5,yMin,2.5,yMax,";track #eta; %s"%yLabel)

                hist0=[]
                hist1=[]
                hist2=[]
                hist3=[]

		hist0.append(f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var)))
		hist1.append(f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var)))
		hist2.append(f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var)))
		hist3.append(f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var)))

		hist0.append(f1.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var)))
		hist1.append(f1.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var)))
		hist2.append(f1.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var)))
		hist3.append(f1.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var)))

		hist0[0].Divide(hist0[1])
		hist1[0].Divide(hist1[1])
		hist2[0].Divide(hist2[1])
		hist3[0].Divide(hist3[1])
                
        
                hist0[0].SetMarkerColor(ROOT.kAzure-9)
                hist1[0].SetMarkerColor(ROOT.kAzure+5)
                hist2[0].SetMarkerColor(ROOT.kAzure+4)
                hist3[0].SetMarkerColor(ROOT.kViolet+1)
### Tracking @ HLT: if you want filled histograms, uncomment
###                hist0[0].SetFillColor(ROOT.kAzure-9)
###                hist1[0].SetFillColor(ROOT.kAzure+5)
###                hist2[0].SetFillColor(ROOT.kAzure+4)
###                hist3[0].SetFillColor(ROOT.kViolet+1)
                if "fake" in var:
                        hist0[0].SetLineColor(ROOT.kAzure-9)
                        hist1[0].SetLineColor(ROOT.kAzure+5)
                        hist2[0].SetLineColor(ROOT.kAzure+4)
                        hist3[0].SetLineColor(ROOT.kViolet+1)
                                
                if "fake" in var:
### Tracking @ HLT: if you want histograms per iteration, uncomment
                        #                     hist2[0].Draw("samep")
                        hist3[0].Draw("samep")
                        hist3[0].SetBinError(0,0)
                        hist3[0].SetBinError(1,0)
                        hist3[0].SetBinError(2,0)
                        hist3[0].SetBinError(3,0)
                        hist2[0].SetBinError(0,0)
                        hist2[0].SetBinError(1,0)
                        hist2[0].SetBinError(2,0)
                        hist2[0].SetBinError(3,0)			
                else:
                        hist3[0].Draw("samehist")
### Tracking @ HLT: if you want histograms per iteration, uncomment
#                        hist2[0].Draw("samehist")
#                        hist1[0].Draw("samehist")
#                        hist0[0].Draw("samehist")
		

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
			
		latex.DrawLatex(0.95, 0.96, "2018 (13 TeV)")
		
		cmsExtra = "#splitline{Simulation}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.84	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		
		leg = TLegend(0.42, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
### Tracking @ HLT: if you want histograms per iteration, uncomment
#		if "fake" in var:
#			leg.AddEntry(hist2[0],"default tracking","p")
#			leg.AddEntry(hist3[0],"with doublet iteration","p")
#		else:
#			leg.AddEntry(hist0[0],"High p_{T} quadruplets","f")
#			leg.AddEntry(hist1[0],"+ Low p_{T} quadruplets","f")
#			leg.AddEntry(hist2[0],"+ Triplets in jets","f")
#			leg.AddEntry(hist3[0],"+ Doublet recovery","f")

		if var == "effic":
			latex.DrawLatex(0.74,0.2,sampleInfo)		
		elif var =="effic_vs_phi":
			latex.DrawLatex(0.59,0.2,sampleInfo)		
		else:	
			latex.DrawLatex(0.89,0.25,sampleInfo)		
		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformance_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_%s.png"%(var))

	
	
main()
