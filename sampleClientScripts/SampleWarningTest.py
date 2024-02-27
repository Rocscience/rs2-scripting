from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_computation_warning_2.fez")
model.compute()

bolt = model.getBoltPropertyByName("Bolt 2")
liner = model.getLinerPropertyByName("Liner 3")

bolt.setBoltType(BoltTypes.FULLY_BONDED)
print(bolt.getBoltType())
