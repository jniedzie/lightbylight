from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.section_('General')
config.General.requestName = 'Aug_reco_pbpb_2015_try2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod_raw_to_reco_data_cfg.py'
#config.JobType.maxMemoryMB = 2400

#config.section_('Data')
#config.Data.inputDataset ='/HIForward/HIRun2015-PromptReco-v1/AOD'  
config.Data.inputDataset ='/HIForward/HIRun2015-v1/RAW'  
#config.Data.inputDBS = 'global'
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt"
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 3500 
config.Data.totalUnits = -1

#config.Data.unitsPerJob = 50
#config.Data.runRange = '262620'
#config.Data.outLFNDirBase = '/store/user/%s/ExpressStream/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.outLFNDirBase = '/store/group/phys_diffraction/diphoton/aug_reco_data_check_for_lumi'
#config.Data.publication = True
config.Data.allowNonValidInputDataset = True

config.Data.outputDatasetTag = config.General.requestName
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_US_Vanderbilt"]
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
