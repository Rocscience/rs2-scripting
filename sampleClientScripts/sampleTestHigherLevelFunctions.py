from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltPropertyByName("Bolt 2")
liner = model.getLinerPropertyByName("Liner 3")

bolt.setBoltType(BoltTypes.FULLY_BONDED)
liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

bolt.FullyBonded.setProperties(BoltDiameter=25.2, OutofPlaneSpacing=1.1, BoltModulusE=50000)
print(str(bolt.FullyBonded.getBoltDiameter()) + ", " + str(bolt.FullyBonded.getOutofPlaneSpacing()) + ", " + str(bolt.FullyBonded.getBoltModulusE()))

liner.ReinforcedConcrete.setProperties(IncludeWeightInAnalysis=True, MaterialType=MaterialType.PLASTIC)
print(str(liner.ReinforcedConcrete.getIncludeWeightInAnalysis()) + ", " + str(liner.ReinforcedConcrete.getMaterialType()))

print(bolt.FullyBonded.getProperties())
print(liner.ReinforcedConcrete.getProperties())