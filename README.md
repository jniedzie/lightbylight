# lightbylight
hiforest trees are made using 
HeavyIonsAnalysis/PhotonAnalysis/plugins/ggHiNtuplizer.cc

to create hiForest, runForestAOD_mod_pbpb_DATA.py used and run in nine following directories over all root files 
HeavyIonsAnalysis/PhotonAnalysis/test/0* 

Trigger trees in hiforest are booked using
HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc


Efficiency
efficiency macros are run on hiforest files obtained in previous step
Reconstruction efficiency codes for HM and GED algo for data and MC, contains corresponding filelist as well
HeavyIonsAnalysis/PhotonAnalysis/test/reco_eff/


ID efficiency codes for HM and GED algo for data and MC, contains corresponding filelist as well
HeavyIonsAnalysis/PhotonAnalysis/test/id_eff/
