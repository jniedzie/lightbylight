# lightbylight
Using CMSSW_7_5_8_patch4 for the analysis 

* hiforest trees are made using 
  HeavyIonsAnalysis/PhotonAnalysis/plugins/ggHiNtuplizer.cc

* to create hiForest, runForestAOD_mod_pbpb_DATA.py used and run in nine following directories over all root files 
  HeavyIonsAnalysis/PhotonAnalysis/test/0* 

* Trigger trees in hiforest are booked using
  HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc


# Efficiency:
efficiency macros are run on hiforest files obtained in previous step
* Reconstruction efficiency codes for HM and GED algo for data and MC with corresponding filelist is in 
  HeavyIonsAnalysis/PhotonAnalysis/test/reco_eff/hybrid/check_data_driven_reco_eff.C


* ID efficiency codes for HM and GED algo for data and MC with corresponding filelist is in 
  HeavyIonsAnalysis/PhotonAnalysis/test/id_eff/hybrid/check_data_driven_id_eff.C

* Submit the efficiency jobs using mysubmit_job.py in each directory, runs on 195 text files, filelist_*.txt

# Reconstruction
  * add all directories to CMSSW_7_5_8_Patch4 and scram
  * aod_raw_to_reco_data_cfg.py runs the reconstruction 
  * crabConfig.py to submit the crab jobs. 
