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
	f1 = TFile("DQM_harvest_partialTemplateCPE_genericIrradiationBiasFalse_afterPR.root","OPEN")
	
	trackCols = ["hltPixel_hltAssociatorByHits","hltIter2PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter2Merged_hltAssociatorByHits","hltIter1PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits"]
	trackLabels = ["pixelTracks","iter2","iter2Merged","iter1","iter0"]
	
	variables = ['efficPt','effic','effic_vs_dr','effic_vs_phi','effic_vs_pu','effic_vs_dxy','fakerate','fakeratePt','fakerate_vs_phi', 'fakerate_vs_pu','duplicatesRate','duplicatesRate_Pt', 'duplicatesRate_pu', 'dxyres_vs_pt', "dzres_vs_pt", "ptres_vs_pt", "phires_vs_pt", "pullPt", "pullPhi", "pullDxy", "pullDz"]
	for var in variables:
                if 'res' in var or "pull" in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMin = 0.0
		yMax = 2.0
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
			plotPad.DrawFrame(0,yMin,120,yMax,";PU; %s"%yLabel)
		elif "dxy" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-1,yMin,1,yMax,";dxy; %s"%yLabel)
		elif "phi" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-3,yMin,3,yMax,";#Phi; %s"%yLabel)
		else:
			plotPad.DrawFrame(-3.0,yMin,3.0,yMax,";track #eta; %s"%yLabel)

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
			
		latex.DrawLatex(0.95, 0.96, yearenergy)
		
		cmsExtra = "#splitline{Simulation}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.84	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		
		leg = TLegend(0.32, 0.72, 0.89, 0.92,legendTitle,"brNDC")
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
	


		canv.Print("HLTTrackingPerformance_ratio_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_ratio_%s.png"%(var))

        ROOT.gStyle.SetPadRightMargin(0.2)
        ROOT.gStyle.SetPalette(55)

	for var in variables:

                if 'res_vs_pt' not in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
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

                for h in xrange(0,2):
                    hist0[h].Scale(1.0/hist0[h].Integral(0,-1,0,-1))
                    hist1[h].Scale(1.0/hist0[h].Integral(0,-1,0,-1))
                    hist2[h].Scale(1.0/hist0[h].Integral(0,-1,0,-1))
                    hist3[h].Scale(1.0/hist0[h].Integral(0,-1,0,-1))
                    print hist3[h].Integral()

		hist0[0].Divide(hist0[1])
		hist1[0].Divide(hist1[1])
		hist2[0].Divide(hist2[1])
		hist3[0].Divide(hist3[1])

                hist3[0].GetZaxis().SetRangeUser(0,2)
                hist3[0].GetZaxis().SetLabelSize(0.02)
                hist3[0].GetZaxis().SetLabelOffset(0.03)
                hist3[0].Draw("samecolz")
		setpalette(hist3[0])
                
                
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
                
#                mean= str("%.2E" % hist3.GetMean(2))
#                rms = str("%.2E" % hist3.GetRMS(2))
		

		leg = TLegend(0.32, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
#                leg.AddEntry(emptyhist, "Mean: %s" % str(mean), "f")
#                leg.AddEntry(emptyhist, "RMS: %s" % str(rms), "f")
                
                latex.DrawLatex(0.89,0.25,sampleInfo)		
		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformance_ratio_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_ratio_%s.png"%(var))


	for var in variables:

                if 'Sigma' not in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMax = 2.0
                yMin = 0.0
		if 'ptres' in var:
			yLabel = '#sigma(p_{T}) ratio'
		elif 'dxyres' in var:	
			yLabel = '#sigma(dxy) ratio'
		elif 'dzres' in var:	
			yLabel = '#sigma(dz) ratio'
		elif 'phires' in var:	
			yLabel = '#sigma(#phi) ratio'

		if "vs_eta" in var:
			plotPad.DrawFrame(-3.0,yMin,3.0,yMax,";track #eta; %s"%yLabel)

		if "vs_phi" in var:
			plotPad.DrawFrame(-3.2,yMin,3.2,yMax,";track #phi; %s"%yLabel)

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

                for h in xrange(0,2):
                    hist0[h].Scale(1.0/hist0[h].Integral(0,-1))
                    hist1[h].Scale(1.0/hist0[h].Integral(0,-1))
                    hist2[h].Scale(1.0/hist0[h].Integral(0,-1))
                    hist3[h].Scale(1.0/hist0[h].Integral(0,-1))
                    print hist3[h].Integral()

		hist0[0].Divide(hist0[1])
		hist1[0].Divide(hist1[1])
		hist2[0].Divide(hist2[1])
		hist3[0].Divide(hist3[1])

                hist3[0].GetZaxis().SetRangeUser(0,2)
                hist3[0].GetZaxis().SetLabelSize(0.02)
                hist3[0].GetZaxis().SetLabelOffset(0.03)
                hist3[0].Draw("same")
#		setpalette(hist3[0])
                
                
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
                
#                mean= str("%.2E" % hist3.GetMean(2))
#                rms = str("%.2E" % hist3.GetRMS(2))
		

		leg = TLegend(0.32, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
#                leg.AddEntry(emptyhist, "Mean: %s" % str(mean), "f")
#                leg.AddEntry(emptyhist, "RMS: %s" % str(rms), "f")
                
                latex.DrawLatex(0.89,0.25,sampleInfo)		
		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformance_ratio_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_ratio_%s.png"%(var))


	for var in variables:

                if 'pull' not in var:
                        continue
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMax = 2.0
                yMin = 0.0
		if 'Pt' in var:
			xLabel = 'p_{T} pull'
		elif 'Dxy' in var:	
			xLabel = 'dxy pull'
		elif 'Dz' in var:	
			xLabel = 'dz pull'
		elif 'Phi' in var:	
			xLabel = '#phi pull'
			
		plotPad.DrawFrame(-10.0,yMin,10.0,yMax,";%s"%xLabel)

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
                
                for h in xrange(0,2):
                    hist0[h].Scale(1.0/hist0[h].Integral(0,-1))
                    hist1[h].Scale(1.0/hist0[h].Integral(0,-1))
                    hist2[h].Scale(1.0/hist0[h].Integral(0,-1))
                    hist3[h].Scale(1.0/hist0[h].Integral(0,-1))

		hist0[0].Divide(hist0[1])
		hist1[0].Divide(hist1[1])
		hist2[0].Divide(hist2[1])
		hist3[0].Divide(hist3[1])
                
                hist3[0].Draw("samehist")
		#setpalette(hist3[0])
                
                
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
                
#                mean= str("%.2E" % hist3.GetMean(2))
#                rms = str("%.2E" % hist3.GetRMS(2))
		
		leg = TLegend(0.32, 0.72, 0.89, 0.92,legendTitle,"brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
#                leg.AddEntry(emptyhist, "Mean: %s" % str(mean), "f")
#                leg.AddEntry(emptyhist, "RMS: %s" % str(rms), "f")
                
                latex.DrawLatex(0.89,0.25,sampleInfo)		
		leg.Draw()	

		plotPad.RedrawAxis()
	
		canv.Print("HLTTrackingPerformance_ratio_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformance_ratio_%s.png"%(var))


	
	
main()
