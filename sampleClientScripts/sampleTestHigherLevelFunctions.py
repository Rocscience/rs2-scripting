from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltPropertyByName("Bolt 2")
liner = model.getLinerPropertyByName("Liner 3")

bolt.FullyBonded.setFullyBondedProperties(BoltDiameter=25.2, OutofPlaneSpacing=1.1, BoltModulusE=50000)
print(str(bolt.FullyBonded.getBoltDiameter()) + ", " + str(bolt.FullyBonded.getOutofPlaneSpacing()) + ", " + str(bolt.FullyBonded.getBoltModulusE()))

liner.ReinforcedConcrete.setReinforcedConcreteProperties(IncludeWeightInAnalysis=True, MaterialType=MaterialType.PLASTIC)
print(str(liner.ReinforcedConcrete.getIncludeWeightInAnalysis()) + ", " + str(liner.ReinforcedConcrete.getMaterialType()))