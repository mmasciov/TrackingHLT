from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle
import ROOT

def setpalette(h2):
    ROOT.gPad.Update()
    palette = h2.GetListOfFunctions().FindObject("palette")
    palette.SetX2NDC(0.925)
    

def main():

        canv = TCanvas("c1","c1",800,800)
	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	style = setTDRStyle()
	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetOptFit(1)
	plotPad.UseCurrentStyle()
	plotPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)
	gStyle.SetTitleYOffset(1.4)

        legendTitle = "XYZ" ### Set according to your needs
        sampleInfo = "#splitline{t#bar{t} event tracks with PU}{|#eta| < 2.5, p_{T}> 0.4 GeV}" ### Set according to your needs
        yearenergy = "2018 (13 TeV)" ### Set according to your needs 

	f0 = TFile("DQM_harvest_generic_std_afterPR.root","OPEN")
	
	trackCols = ["hltPixel_hltAssociatorByHits","hltIter2PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter2Merged_hltAssociatorByHits","hltIter1PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits"]
	trackLabels = ["pixelTracks","iter2","iter2Merged","iter1","iter0"]
	
	variables = ['efficPt','effic','effic_vs_dr','effic_vs_phi','effic_vs_pu','effic_vs_dxy','fakerate','fakeratePt','fakerate_vs_phi', 'fakerate_vs_pu','duplicatesRate','duplicatesRate_Pt', 'duplicatesRate_pu', 'dxyres_vs_pt', "dzres_vs_pt", "ptres_vs_pt", "phires_vs_pt", "pullPt", "pullPhi", "pullDxy", "pullDz", "dzres_vs_eta_Sigma", "dzres_vs_phi_Sigma", "dxyres_vs_eta_Sigma", "dxyres_vs_phi_Sigma", "ptres_vs_eta_Sigma", "ptres_vs_phi_Sigma", "phires_vs_eta_Sigma", "phires_vs_phi_Sigma"]

        ROOT.gStyle.SetOptStat(0)

	for var in variables:
                if 'res' in var or 'pull' in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMax = 1.2
		if 'effic' in var:
			yLabel = 'HLT Tracking Efficiency'
		elif 'fake' in var:	
			yLabel = 'Fake Rate'
			#plotPad.SetLogy()			
                        #yMin=0
			yMax=1.0
		elif 'dupli' in var:	
			yLabel = 'Duplicate Rate'
                        yMax=0.02
			
		if "Pt" in var:
			plotPad.SetLogx()
			plotPad.DrawFrame(0,0.001,200,yMax,";track p_{T} [GeV]; %s"%yLabel)
		elif "dr" in var:
			plotPad.SetLogx()
			plotPad.DrawFrame(0,0.001,1,yMax,";dR; %s"%yLabel)
		elif "pu" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(0,0.001,120,yMax,";PU; %s"%yLabel)
		elif "dxy" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-1,0.002,1,yMax,";dxy; %s"%yLabel)
		elif "phi" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-3,0.001,3,yMax,";#Phi; %s"%yLabel)
		else:
			plotPad.DrawFrame(-3,0.001,3,yMax,";track #eta; %s"%yLabel)

		hist0 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var))
		hist1 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var))
		hist2 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var))
		hist3 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var))


                f1 = TF1("f1", "pol1", 0, 120);
		
		hist0.SetMarkerColor(ROOT.kAzure-9)
		hist1.SetMarkerColor(ROOT.kAzure+5)
		hist2.SetMarkerColor(ROOT.kAzure+4)
		hist3.SetMarkerColor(ROOT.kViolet+1)
### Tracking @ HLT: if you want filled histograms, uncomment
###		hist0.SetFillColor(ROOT.kAzure-9)
###		hist1.SetFillColor(ROOT.kAzure+5)
###		hist2.SetFillColor(ROOT.kAzure+4)
###		hist3.SetFillColor(ROOT.kViolet+1)
		if "fake" in var:
			hist0.SetLineColor(ROOT.kAzure-9)
			hist1.SetLineColor(ROOT.kAzure+5)
			hist2.SetLineColor(ROOT.kAzure+4)
			hist3.SetLineColor(ROOT.kViolet+1)

		if "fake" in var:
### Tracking @ HLT: if you want histograms per iteration, uncomment
#			hist2.Draw("samep")
			hist3.Draw("samep")
			hist3.SetBinError(0,0)
			hist3.SetBinError(1,0)
			hist3.SetBinError(2,0)
			hist3.SetBinError(3,0)
			hist2.SetBinError(0,0)
			hist2.SetBinError(1,0)
			hist2.SetBinError(2,0)
			hist2.SetBinError(3,0)			
		else:
			hist3.Draw("samehist")
### Tracking @ HLT: if you want histograms per iteration, uncomment
#			hist2.Draw("samehist")
#			hist1.Draw("samehist")
#			hist0.Draw("samehist")
		
                if "pu" in var:
                    hist3.Fit("f1", "b")
                    f1.Draw("same")

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
			
		latex.DrawLatex(0.95, 0.96, yearenergy)
		
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
#			leg.AddEntry(hist2,"default tracking","p")
#			leg.AddEntry(hist3,"with doublet iteration","p")
#		else:
#			leg.AddEntry(hist0,"High p_{T} quadruplets","f")
#			leg.AddEntry(hist1,"+ Low p_{T} quadruplets","f")
#			leg.AddEntry(hist2,"+ Triplets in jets","f")
#			leg.AddEntry(hist3,"+ Doublet recovery","f")

		if var == "effic":
			latex.DrawLatex(0.74,0.2,sampleInfo)		
		elif var =="effic_vs_phi":
			latex.DrawLatex(0.59,0.2,sampleInfo)		
		else:	
			latex.DrawLatex(0.89,0.25,sampleInfo)		
#		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformance_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_%s.png"%(var))


        ROOT.gStyle.SetPadRightMargin(0.2)
        ROOT.gStyle.SetPalette(55)

	for var in variables:

                if 'res_vs_pt' not in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		plotPad.SetLogz()
		yMax = 0.1
                yMin = -0.1
		if 'ptres' in var:
			yLabel = 'p_{T} resolution'
		elif 'dxyres' in var:	
			yLabel = 'dxy resolution'
		elif 'dzres' in var:	
			yLabel = 'dz resolution'
		elif 'phires' in var:	
			yLabel = '#phi resolution'
                        yMax=0.01
                        yMin=-0.01
		
		if "vs_pt" in var:
#			plotPad.SetLogx()
			plotPad.DrawFrame(0,yMin,200,yMax,";track p_{T} [GeV]; %s"%yLabel)

		hist0 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var))
		hist1 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var))
		hist2 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var))
		hist3 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var))
                
                #hist3.GetZaxis().SetRangeUser(0,2)
                hist3.GetZaxis().SetLabelSize(0.02)
                hist3.GetZaxis().SetLabelOffset(0.03)
                hist3.Draw("samecolz")
		setpalette(hist3)

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
			
		latex.DrawLatex(0.95, 0.96, yearenergy)
		
		cmsExtra = "#splitline{Simulation}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.84	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		emptyhist = TH1D("emptyhist","",1,0,1)
                emptyhist.SetFillColor(0)
                emptyhist.SetLineColor(0)
                
                mean= str("%.2E" % hist3.GetMean(2))
                rms = str("%.2E" % hist3.GetRMS(2))
		
		leg = TLegend(0.42, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
                leg.AddEntry(emptyhist, "Mean: %s" % str(mean), "f")
                leg.AddEntry(emptyhist, "RMS: %s" % str(rms), "f")
                
                latex.DrawLatex(0.89,0.25,sampleInfo)		
#		leg.Draw()	

		plotPad.RedrawAxis()
	


#		canv.Print("HLTTrackingPerformance_modified_%s.pdf"%(var))
#		canv.Print("HLTTrackingPerformance_modified_%s.png"%(var))
		canv.Print("HLTTrackingPerformance_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_%s.png"%(var))


	for var in variables:

                if 'Sigma' not in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		plotPad.SetLogz()
		yMax = 0.1
                yMin = 0.0
		if 'ptres' in var:
			yLabel = '#sigma(p_{T})'
		elif 'dxyres' in var:	
			yLabel = '#sigma(dxy)'
		elif 'dzres' in var:	
			yLabel = '#sigma(dz)'
		elif 'phires' in var:	
			yLabel = '#sigma(#phi)'
                        yMax=0.1
                        yMin=0.0
		
		if "vs_eta" in var:
			plotPad.DrawFrame(-3.0,yMin,3.0,yMax,";track #eta; %s"%yLabel)

		if "vs_phi" in var:
			plotPad.DrawFrame(-3.2,yMin,3.2,yMax,";track #phi; %s"%yLabel)

		hist0 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var))
		hist1 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var))
		hist2 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var))
		hist3 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var))
                
                #hist3.GetZaxis().SetRangeUser(0,2)
                hist3.GetZaxis().SetLabelSize(0.02)
                hist3.GetZaxis().SetLabelOffset(0.03)
                hist3.Draw("same")
#		setpalette(hist3)

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
			
		latex.DrawLatex(0.95, 0.96, yearenergy)
		
		cmsExtra = "#splitline{Simulation}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.84	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		emptyhist = TH1D("emptyhist","",1,0,1)
                emptyhist.SetFillColor(0)
                emptyhist.SetLineColor(0)
                
                mean= str("%.2E" % hist3.GetMean(2))
                rms = str("%.2E" % hist3.GetRMS(2))
		
		leg = TLegend(0.42, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
#                leg.AddEntry(emptyhist, "Mean: %s" % str(mean), "f")
#                leg.AddEntry(emptyhist, "RMS: %s" % str(rms), "f")
                
                latex.DrawLatex(0.89,0.65,sampleInfo)		
		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformance_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_%s.png"%(var))


	for var in variables:

                if 'pull' not in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		plotPad.SetLogz()
		yMax = 0.75e5
		if 'Pt' in var:
			xLabel = 'p_{T} pull'
		elif 'Dxy' in var:	
			xLabel = 'dxy pull'
		elif 'Dz' in var:	
			xLabel = 'dz pull'
		elif 'Phi' in var:	
			xLabel = '#phi pull'
		
                plotPad.DrawFrame(-10,0,10,yMax,";%s;Tracks"%xLabel)

		hist0 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var))
		hist1 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var))
		hist2 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var))
		hist3 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var))
                
                hist3.Draw("samehist")
		
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
			
		latex.DrawLatex(0.95, 0.96, yearenergy)
		
		cmsExtra = "#splitline{Simulation}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.84	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		emptyhist = TH1D("emptyhist","",1,0,1)
                emptyhist.SetFillColor(0)
                emptyhist.SetLineColor(0)
                
                mean= str("%.2E" % hist3.GetMean(1))
                rms = str("%.2E" % hist3.GetRMS(1))
		
		leg = TLegend(0.42, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
                leg.AddEntry(emptyhist, "Mean: %s" % str(mean), "f")
                leg.AddEntry(emptyhist, "RMS: %s" % str(rms), "f")
                
                latex.DrawLatex(0.89,0.25,sampleInfo)		
#		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformance_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_%s.png"%(var))
	
main()
