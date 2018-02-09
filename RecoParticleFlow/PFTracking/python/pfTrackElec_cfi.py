import FWCore.ParameterSet.Config as cms

pfTrackElec = cms.EDProducer("PFElecTkProducer",
    TrajInEvents = cms.bool(False),
    Fitter = cms.string('GsfElectronFittingSmoother'),
    ModeMomentum = cms.bool(True),
    applyEGSelection = cms.bool(False),        
    applyGsfTrackCleaning = cms.bool(True),
    applyAlsoGsfAngularCleaning = cms.bool(True),
    maxDEtaGsfAngularCleaning = cms.double(0.05),
    maxDPhiBremTangGsfAngularCleaning = cms.double(0.05),                         
    useFifthStepForTrackerDrivenGsf = cms.bool(False),
    useFifthStepForEcalDrivenGsf = cms.bool(False),                         
    MaxConvBremRecoPT = cms.double(49.0),                         
    MinDEtaGsfSC = cms.double(0.06),
    MinDPhiGsfSC = cms.double(0.15),
    MinSCEnergy = cms.double(1.0),                         
    TTRHBuilder = cms.string('WithTrackAngle'),
    GsfTrackModuleLabel = cms.InputTag("electronGsfTracks"),
    Propagator = cms.string('fwdElectronPropagator'),
    PFRecTrackLabel = cms.InputTag("pfTrack"),
    PFEcalClusters  = cms.InputTag("particleFlowClusterECAL"),                 
    PrimaryVertexLabel = cms.InputTag("offlinePrimaryVertices"),                         
    useConvBremFinder  = cms.bool(True),
    PFNuclear = cms.InputTag("pfDisplacedTrackerVertex"),
    PFConversions = cms.InputTag("pfConversions"),
    PFV0 = cms.InputTag("pfV0"),
    useNuclear = cms.bool(False),
    useV0 = cms.bool(False), 
    useConversions = cms.bool(False),
    debugGsfCleaning = cms.bool(False),
    AbsEtaBarrelEndcapsSeparation = cms.double(1.479),
    PtLowHighSeparation = cms.double(20),                         
    pf_convBremFinderID_mvaCutBarrelLowPt =  cms.double(0.6),
    pf_convBremFinderID_mvaCutBarrelHighPt =  cms.double(0.97),
    pf_convBremFinderID_mvaCutEndcapsLowPt =  cms.double(0.9),
    pf_convBremFinderID_mvaCutEndcapsHighPt =  cms.double(0.995),
    pf_convBremFinderID_mvaWeightFileBarrelLowPt = cms.string('RecoParticleFlow/PFTracking/data/TMVAClassification_ConvBremFinder_Testetlt20absetalt1_479_BDT.weights.xml'),
    pf_convBremFinderID_mvaWeightFileBarrelHighPt = cms.string('RecoParticleFlow/PFTracking/data/TMVAClassification_ConvBremFinder_Testetgt20absetalt1_479_BDT.weights.xml'),
    pf_convBremFinderID_mvaWeightFileEndcapsLowPt = cms.string('RecoParticleFlow/PFTracking/data/TMVAClassification_ConvBremFinder_Testetlt20absetagt1_479_BDT.weights.xml'),
    pf_convBremFinderID_mvaWeightFileEndcapsHighPt = cms.string('RecoParticleFlow/PFTracking/data/TMVAClassification_ConvBremFinder_Testetgt20absetagt1_479_BDT.weights.xml')
)


