from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle
import os
gROOT.SetBatch()
import subprocess
def main():
	
	canv = TCanvas("c1","c1",800,800)

	plotPad = TPad("plotPad","plotPad",0,0.3,1,1)
	ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	ratioPad.Draw()	
	plotPad.cd()
	plotPad.SetGrid()

	
	f0 = TFile("DQM_harvest_generic_std_afterPR.root","OPEN")
	f1 = TFile("DQM_harvest_generic_std_afterPR.root","OPEN")
	f2 = TFile("DQM_harvest_partialTemplateCPE_genericIrradiationBiasFalse_afterPR.root","OPEN")

	doNotNormalize = [
		"Chi2oNDFVsEta_ImpactPoint_GenTk",
		"Chi2oNDFVsNHits_ImpactPoint_GenTk",
		"Chi2oNDFVsPt_ImpactPoint_GenTk",
		"DistanceOfClosestApproachToBSVsPhi_GenTk",
		"DistanceOfClosestApproachToPVVsPhi_GenTk",
		"NumberOfTracksVsLS_GenTk",
		"NumberOfGoodPVtxVsLS_GenTk",
		"NumberOfGoodPVtxWO0VsLS_GenTk",
		"NumberOfLayersPerTrackVsEta_ImpactPoint_GenTk",
		"NumberOfLayersPerTrackVsPhi_ImpactPoint_GenTk",
		"NumberOfRecHitsPerTrackVsEta_ImpactPoint_GenTk",
		"NumberOfRecHitsPerTrackVsPhi_ImpactPoint_GenTk",
		"NumberOfRecHitsPerTrackVsLS_GenTk",
		"NumberOfTracksVsLS_GenTk",
		"NumberOfValidRecHitsPerTrackVsEta_ImpactPoint_GenTk",
		"NumberOfValidRecHitsPerTrackVsPhi_ImpactPoint_GenTk",
		"NumberOfValidRecHitsPerTrackVsPt_ImpactPoint_GenTk",
		"TrackPtErrOverPtVsEta_ImpactPoint_GenTk",
		"stoppingSourceVSeta_GenTk",
		"stoppingSourceVSphi_GenTk",
		"xPointOfClosestApproachVsZ0wrt000_GenTk",
		"xPointOfClosestApproachVsZ0wrtBS_GenTK",
		"xPointOfClosestApproachVsZ0wrtPV_GenTk",
		"yPointOfClosestApproachVsZ0wrt000_GenTk",
		"yPointOfClosestApproachVsZ0wrtBS_GenTK",
		"yPointOfClosestApproachVsZ0wrtPV_GenTk",
		"zPointOfClosestApproachVsPhi_GenTk",
	
	]
	
	doNotNormalizeDir = [
		"HitEffFromHitPattern",
		"HitEffFromHitPatternAll",
		"HitEffFromHitPatternVsBX",
		"HitProperties",
		"PUmonitoring",
		"BXanalysis"
	
	]
		
	
	yRanges = {
	
		"DistanceOfClosestApproachToBSVsPhi_GenTk": [-0.005,0.005],
		"DistanceOfClosestApproachToPVVsPhi_GenTk": [-0.005,0.005],	
		"NumberOfLayersPerTrackVsPhi_ImpactPoint_GenTk": [8,12],	
		"NumberOfRecHitsPerTrackVsPhi_ImpactPoint_GenTk": [8,12],	
		"NumberOfValidRecHitsPerTrackVsPhi_ImpactPoint_GenTk": [8,12],	
		"stoppingSourceVSeta_GenTk": [0.2,0.7],	
		"stoppingSourceVSphi_GenTk": [0.2,0.7],	
		"xPointOfClosestApproachVsZ0wrt000_GenTk": [-0.04,0.04],	
		"yPointOfClosestApproachVsZ0wrt000_GenTk": [-0.1,0.1],	
	}
	
	trackCols = ["tracks","pixelTracks"]
	trackLabels = ["pixelTracks","iter2","iter2Merged","iter1","iter0"]
	
	#dirs = ["BXanalysis","GeneralProperties","HitEffFromHitPattern","HitEffFromHitPatternAll","HitEffFromHitPatternVsBX","HitProperties","LUMIanalysis","PUmonitoring"]
	dirs = ["BXanalysis","GeneralProperties","HitProperties","LUMIanalysis","PUmonitoring"]

	for name in trackCols:
		for dir in dirs:
			useName = name
			f0.cd("DQMData/Run 1/HLT/Run summary/Tracking/%s/%s"%(name,dir))
			hists = gDirectory.GetListOfKeys()
			print hists
			for hist in hists: 
				hist0 = hist.ReadObj()			
				histName = hist0.GetName()	
							
				if not "TrackEtaPhi" in histName and not hist0.ClassName() == "TObjString" and not hist0.ClassName() == "TDirectoryFile" and not hist0.ClassName() == "TProfile2D" and not hist0.ClassName() == "TH2F":

					
					histName = hist0.GetName()
					hist1 = f1.Get("DQMData/Run 1/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
					hist2 = f2.Get("DQMData/Run 1/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))

					if "NumberOfTracks_GenTk" in histName:
						hist0.GetXaxis().SetRangeUser(0,250)
						hist1.GetXaxis().SetRangeUser(0,250)
						hist2.GetXaxis().SetRangeUser(0,250)
						
					hist0.Sumw2()
					hist1.Sumw2()				
					hist2.Sumw2()				
#					if hist0.GetYaxis().GetTitle() == "Number of Tracks" or hist0.GetYaxis().GetTitle() == "Number of Events" or hist0.GetYaxis().GetTitle() == "Number of events" or hist0.GetYaxis().GetTitle() == "Entries":
							
#						if hist0.GetEntries() > 0:
#							hist0.Scale(1./hist0.GetEntries())
#						if hist1.GetEntries() > 0:
#							hist1.Scale(1./hist1.GetEntries())
#						if hist2.GetEntries() > 0:
#							hist2.Scale(1./hist2.GetEntries())
					print histName
					print hist0.ClassName()

					hist2.SetMarkerColor(kBlue)
					hist1.SetMarkerColor(kRed)
					
					hist2.SetLineColor(kBlue)
					hist1.SetLineColor(kRed)
				
					hist2.SetLineWidth(2)
					hist1.SetLineWidth(2)
				
					
					if min(hist1.GetMinimum(),hist0.GetMinimum()) < 0:
						yMin = min(hist1.GetMinimum(),hist0.GetMinimum())*1.25
					else:
						yMin = min(hist1.GetMinimum(),hist0.GetMinimum())*0.75
					yMax = max(hist1.GetMaximum(),hist0.GetMaximum())*1.55
						
				
						
					hist1.GetYaxis().SetRangeUser(yMin,yMax)
					hist1.Draw("hist")
					hist2.Draw("samehist")
					
			
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
					
					cmsExtra = "Simulation"
					latexCMS.DrawLatex(0.19,0.88,"CMS")
					if "Simulation" in cmsExtra:
						yLabelPos = 0.81	
					else:
						yLabelPos = 0.84	

					latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

					
					leg = TLegend(0.32, 0.71, 0.89, 0.92,"t#bar{t} MC with PU","brNDC")
					leg.SetFillColor(10)
					leg.SetFillStyle(0)
					leg.SetLineColor(10)
					leg.SetShadowColor(0)
					leg.SetBorderSize(1)		
					if "DistanceOfClosestApproach" in histName:
						leg.AddEntry(hist1,"Generic CPE (w/o correction)","p")
						leg.AddEntry(hist2,"Template CPE (fit; w/o correction)","p")					
					else:
						leg.AddEntry(hist1,"Generic CPE (w/o correction)","p")
						leg.AddEntry(hist2,"Template CPE (fit; w/o correction)","p")					
					leg.Draw()
					ratioPad.cd()
					
					if hist0.ClassName() == "TProfile":
						
						ratio = hist1.Clone("")
						ratio2 = hist1.Clone("")
						toDivide = hist0.Clone("")
						toDivide2 = hist2.Clone("")
						
						for i in range(0,hist0.GetNbinsX()+1):
							ratio.SetBinError(i,abs(ratio.GetBinContent(i))**0.5)
							ratio2.SetBinError(i,abs(ratio2.GetBinContent(i))**0.5)
							toDivide.SetBinError(i,abs(toDivide.GetBinContent(i))**0.5)
							toDivide2.SetBinError(i,abs(toDivide2.GetBinContent(i))**0.5)
						ratio.Sumw2()
						ratio2.Sumw2()
						toDivide.Sumw2()
						toDivide2.Sumw2()
						ratio.Divide(toDivide)
						ratio2.Divide(toDivide2)
					else:
						ratio = hist1.Clone("")
						ratio.Divide(hist0)
						ratio2 = hist1.Clone("")
						ratio2.Divide(hist2)
					ratio.SetLineColor(hist0.GetLineColor())
					ratio.SetMarkerColor(hist0.GetMarkerColor())
					ratio2.SetLineColor(hist2.GetLineColor())
					ratio2.SetMarkerColor(hist2.GetMarkerColor())
					ratio2.GetYaxis().SetRangeUser(0,2)
					ratio2.GetYaxis().SetTitle("Generic/Template")
#					ratio2.GetYaxis().SetTitle("Before/After")
#					ratio2.GetYaxis().SetTitle("Without/With")
					ratio2.GetYaxis().SetTitleSize(0.1)
					ratio2.GetYaxis().SetTitleOffset(0.3)
					
					ratio2.Draw("pe0")
					line = TLine(ratio.GetBinCenter(1),1,ratio.GetBinCenter(ratio.GetNbinsX()),1)
					line.SetLineStyle(kDashed)
					line.Draw("same")
					if not os.path.exists(name):
						os.makedirs(name)
					if not os.path.exists(name+"/"+dir):
						os.makedirs(name+"/"+dir)
					
					plotPad.RedrawAxis()
					canv.Print(name+"/"+dir+"/"+"DQM_%s_%s.pdf"%(name,histName))
					canv.Print(name+"/"+dir+"/"+"DQM_%s_%s.png"%(name,histName))

			subprocess.call(["cp","index.php","%s/%s/"%(name,dir)])
		subprocess.call(["cp","index.php","%s"%(name)])	
	
main()
