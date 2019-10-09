
import FWCore.ParameterSet.Config as cms

from Validation.RecoTrack.HLTmultiTrackValidator_cff import *

doPixel = True
doTrack02 = True

hltTrackValidator.label = []
if doPixel:
	hltTrackValidator.label.extend([
    		"hltPixelTracks",
    		"hltPixelTracksFromTriplets",
    		"hltPixelTracksMerged"
	])
if doTrack02:
	hltTrackValidator.label.extend([
    		"hltIter0PFlowTrackSelectionHighPurity",
    		"hltIter1PFlowTrackSelectionHighPurity",
    		"hltIter1Merged",
     		"hltIter2PFlowTrackSelectionHighPurity",
    		"hltIter2Merged",
    		"hltTripletRecoveryPFlowTrackSelectionHighPurity",
    		"hltTripletRecoveryMerged",
  		"hltDoubletRecoveryPFlowTrackSelectionHighPurity",
    		"hltMergedTracks"
	])

hltTrackValidator.cores = cms.InputTag("")

from SimGeneral.TrackingAnalysis.trackingParticleNumberOfLayersProducer_cfi import *
#hltTracksValidationTruth = cms.Sequence(hltTPClusterProducer+hltTrackAssociatorByHits+trackingParticleRecoTrackAsssociation+VertexAssociatorByPositionAndTracks+trackingParticleNumberOfLayersProducer)
hltTracksValidationTruth = cms.Sequence(hltTPClusterProducer+hltTrackAssociatorByHits+trackingParticleNumberOfLayersProducer)


hltMultiTrackValidation = cms.Sequence(
    hltTracksValidationTruth
    + hltTrackValidator
)
#from Validation.RecoTrack.associators_cff import *


from SimTracker.VertexAssociation.VertexAssociatorByPositionAndTracks_cfi import *
hltVertexAssociatorByPositionAndTracks = VertexAssociatorByPositionAndTracks.clone()
hltVertexAssociatorByPositionAndTracks.trackAssociation = "tpToHLTpixelTrackAssociation"

from Validation.RecoVertex.HLTmultiPVvalidator_cff import *
hltMultiPVanalysis.verbose = False
#hltMultiPVanalysis.trackAssociatorMap = "tpToHLTpixelTrackAssociation"
#hltMultiPVanalysis.vertexAssociator   = "vertexAssociatorByPositionAndTracks4pixelTracks"
#tpToHLTpixelTrackAssociation.ignoremissingtrackcollection = False
hltPixelPVanalysis.trackAssociatorMap = "tpToHLTpixelTrackAssociation"
hltPixelPVanalysis.vertexAssociator = "vertexAssociatorByPositionAndTracks4pixelTracks" 

tpToHLTpixelTrackAssociation.label_tr = "hltPixelTracksMerged"

validation = cms.EndPath(
    hltMultiTrackValidation
    + hltTrackAssociatorByHits
    + tpToHLTpixelTrackAssociation
    + hltVertexAssociatorByPositionAndTracks
#    + hltMultiPVanalysis
    + hltMultiPVValidation
)


dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)
DQMOutput = cms.EndPath( dqmOutput )

