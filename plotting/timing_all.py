from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle
import sys,os

isData = True
dataormc = "data"
if len(sys.argv)>1:
        dataormc=str(sys.argv[1])
if(dataormc=="MC" or dataormc=="mc" or dataormc=="Mc" or dataormc=="mC"):
        isData = False

outdir = "Timing_"
if isData:
        outdir = outdir+"data"
else:
        outdir = outdir+"mc"

def main():
        
        canv = TCanvas("c1","c1",800,800)
                
		
	fIdeal = TFile("DQM_timeHarvest_genericCPE_irradiationBiasTrue_afterPR.root","OPEN")
	fCPE = TFile("DQM_timeHarvest_templateCPE_irradiationBiasFalse_afterPR.root","OPEN")        
        
        fIdeal.cd("DQMData/Run 1/HLT/Run summary/TimerService/process TEST modules/")
        hists = gDirectory.GetListOfKeys()
        print hists
        for h in hists:
                cl = gROOT.GetClass(h.GetClassName())
                if not cl.InheritsFrom("TH1"):
                        continue
                hist0 = h.ReadObj()
                histName = hist0.GetName()
                if "time_real" not in histName or "byls" in histName or "hlt" not in histName:
                        continue
                #print histName
                moduleName = histName.split()[0]
                #print moduleName
                
                histIdeal = fIdeal.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST modules/"+histName)
                histCPE = fCPE.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST modules/"+histName)
                
                histIdeal.Rebin(5)
                histCPE.Rebin(5)

                plotPad = TPad("plotPad","plotPad",0,0,1,1)
                style = setTDRStyle()
                gStyle.SetTitleYOffset(1.45)
                gStyle.SetOptStat(0)
                plotPad.UseCurrentStyle()
                plotPad.Draw()	
                plotPad.cd()
                #plotPad.DrawFrame(0,0.2,200,50000,";time [ms]; Events / 5 ms")
        	plotPad.DrawFrame(0,0.2,2000,15000,";time [ms]; Events / 5 ms")
                plotPad.SetLogy()


                histIdeal.Draw("samehist")
                histIdeal.SetLineColor(kRed)
                histCPE.SetLineColor(kBlue)
                histCPE.Draw("samehist")
                

                leg = TLegend(0.42, 0.61, 0.89, 0.92,moduleName,"brNDC")
                leg.SetFillColor(10)
                leg.SetLineColor(10)
                leg.SetShadowColor(0)
                leg.SetBorderSize(1)		
                leg.AddEntry(histIdeal,"Generic CPE w/ correction %.2f ms"%histIdeal.GetMean(),"l")
                leg.AddEntry(histCPE,"Template CPE w/o correction %.2f ms"%histCPE.GetMean(),"l")
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
                
                #cmsExtra = "Preliminary"
                cmsExtra = "Simulation"
                latexCMS.DrawLatex(0.19,0.88,"CMS")
                if "Simulation" in cmsExtra:
                        yLabelPos = 0.81	
                else:
                        yLabelPos = 0.84	
                        
                latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				
                                
                if not os.path.exists(outdir):
                        os.makedirs(outdir)
                canv.Print(outdir+"/timingIO_"+moduleName+"_TTbarMC_GenericVsTemplateCPE_wNwoCorrection.pdf")
                canv.Print(outdir+"/timingIO_"+moduleName+"_TTbarMC_GenericVsTemplateCPE_wNwoCorrection.png")
                
                canv.Update()
                canv.Clear()
                
                del histIdeal
                del histCPE
                
main()
