from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
pile = model.getAllPileProperties()[0]
pile.setConnectionType(PileConnectionType.HINGED)
pile.setSkinResistance(PileSkinResistanceType.MULTI_LINEAR)
print(pile.getConnectionType())

pile.Beam.setApplication(PileApplicationType.DEFINE_BEAM_SEGMENT_BY_LENGTH)
pile.Beam.defineBeamSegment([3], ["Liner 4", "Liner 5"])

print(pile.Beam.getBeamSegment())