import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
   comEnergy = cms.double(7000.0),
   crossSection = cms.untracked.double(0.2141),
   filterEfficiency = cms.untracked.double(1),
   maxEventsToPrint = cms.untracked.int32(0),
   pythiaHepMCVerbosity = cms.untracked.bool(True),
   pythiaPylistVerbosity = cms.untracked.int32(1),

   PythiaParameters = cms.PSet(
      processParameters = cms.vstring(
         'Main:timesAllowErrors    = 10000',
         'ParticleDecays:limitTau0 = on',
         'ParticleDecays:tauMax = 10',
         'Tune:pp 5',
         'Tune:ee 3',
         'PDF:pSet = 5',
         'ExtraDimensionsLED:ffbar2llbar = on', 
         'ExtraDimensionsLED:gg2llbar = on', 
         'PhaseSpace:mHatMin = 400',
         'ExtraDimensionsLED:CutOffmode = 0',
         'ExtraDimensionsLED:LambdaT = 3200'
      ),
      parameterSets = cms.vstring('processParameters')
   )
)

configurationMetadata = cms.untracked.PSet(
   version = cms.untracked.string('\$Revision: 1.1 $'),
   name = cms.untracked.string('\$Source: /cvs/CMSSW/CMSSW/Configuration/GenProduction/python/ADDdilepton_LambdaT_3200_7TeV_pythia8_cff.py,v $'),
   annotation = cms.untracked.string('Summer2011 sample with PYTHIA8: ADD Dilepton samples with LambdaT = 3200 GeV, Tune4C, pdf: MSTW 2008 LO')
)
