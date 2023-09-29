from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
pile = model.getAllPileProperties()[0]
pile.setConnectionType(PileConnectionType.CONNECT_HINGED)
pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
print(pile.getConnectionType())

pile.Beam.setLinerProperty("Liner 7")
print(pile.Beam.getLinerProperty())
pile.Beam.setLinerProperty("Liner 5")
print(pile.Beam.getLinerProperty())
pile.Beam.setLinerProperty("Liner 1")
print(pile.Beam.getLinerProperty())
pile.Beam.setLinerProperty("Liner 4")
print(pile.Beam.getLinerProperty())