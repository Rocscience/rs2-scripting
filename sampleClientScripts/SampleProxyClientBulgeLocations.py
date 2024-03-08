from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile('C:/Intel/simple_3_stage.fez')
bolt = model.getAllBoltProperties()[0]

bolt.setBoltType(BoltTypes.PLAIN_STRAND_CABLE)
bolt.PlainStrandCable.setAddBulges(True)

bolt.PlainStrandCable.setBulgeLocations([26,63,82])
print(bolt.PlainStrandCable.getBulgeLocations())