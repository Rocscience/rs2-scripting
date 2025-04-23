from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]

bolt1.setBoltName("Example Bolt 1")
bolt1.setBoltType(BoltTypes.FULLY_BONDED)
bolt1.FullyBonded.setBoltDiameter(28)
bolt1.FullyBonded.setJointShear(True)
bolt1.FullyBonded.setPreTensioningForce(0.2)

print(bolt1.FullyBonded.getBoltDiameter())
print(bolt1.FullyBonded.getJointShear())
print(bolt1.FullyBonded.getPreTensioningForce())

bolt2.setBoltName("Example Bolt 2")
bolt2.setBoltType(BoltTypes.END_ANCHORED)
bolt2.EndAnchored.setProperties(BoltModulusE=250000, OutofPlaneSpacing=1.2, TensileCapacity=0.2)

print(bolt2.EndAnchored.getProperties())

bolt3.setBoltName("Example Bolt 3")
bolt3.setBoltType(BoltTypes.PLAIN_STRAND_CABLE)
bolt3.PlainStrandCable.setProperties(AddBulges=True, AddPullOutForce=True, PullOutForce=1)
# Not all functions are accessible through the setProperties method. 
# Consult setProperties method definition in documentation to determine properties available.
bolt3.PlainStrandCable.setBulgeLocations([10,20,30])

print(bolt3.PlainStrandCable.getProperties())
# Not all functions are accessible through the getProperties method. 
# Consult getProperties method definition in documentation to determine properties available.
print(bolt3.PlainStrandCable.getBulgeLocations())

model.close()
modeler.closeProgram()