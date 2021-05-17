import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.sortedPackedPrimaryVertices_cfi import sortedPackedPrimaryVertices

primaryVertexAssociation = sortedPackedPrimaryVertices.clone(
  qualityForPrimary = 2,
  produceSortedVertices = False,
  producePileUpCollection  = False,
  produceNoPileUpCollection = False
)
