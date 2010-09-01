import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(6.769),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),        
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('PMAS(42,1)=200.0        ! LQ mass', 
            'IMSS(21)=33             ! LUN number for SLHA File (must be 33)',             
            'IMSS(22)=33             ! Read-in SLHA decay table',
            'KCHG(42,1)=2            ! LQ charge x 3',  
            'MSEL=0                  ! (D=1) to select between full user control (0, then use MSUB) and some preprogrammed alternative', 
            'MSUB(163)=1             ! g+g->LQ+LQbar', 
            'MSUB(164)=1             ! q+qbar->LQ+LQbar'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters',
            'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = Configuration/Generator/data/LQ_btau_beta1.0.out')
    )
)

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.2 $'),
        name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/Configuration/GenProduction/python/PYTHIA6_Tauola_Exotica_LQ_btau_200_7TeV_tautaubb_cff.py,v $'),
        annotation = cms.untracked.string('default documentation string for PYTHIA6_Tauola_Exotica_LQ_btau_200_7TeV_tautaubb_cff.py')
)

ProductionFilterSequence = cms.Sequence(generator)
