import FWCore.ParameterSet.Config as cms
from CommonTools.ParticleFlow.pfNoPileUpJME_cff import adapt, pfPileUpJME
from PhysicsTools.PatAlgos.primaryVertexAssociation_cfi import primaryVertexAssociation

primaryVertexAssociationJME = primaryVertexAssociation.clone()
adapt(primaryVertexAssociationJME)

pfNoPileUpJME = cms.EDProducer("PFnoPileUp",
  candidates = cms.InputTag("packedPFCandidates"),
  vertexAssociationQuality = pfPileUpJME.vertexAssociationQuality,
  vertexAssociation = pfPileUpJME.vertexAssociation
  )
