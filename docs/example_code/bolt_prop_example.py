from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]

#Assigning bolt1 properties individually
bolt1.setBoltName("Example Bolt 1")
bolt1.setBoltType(BoltTypes.FULLY_BONDED)
bolt1.FullyBonded.setBoltDiameter(28)
bolt1.FullyBonded.setJointShear(True)
bolt1.FullyBonded.setPreTensioningForce(0.2)

#Retrieving bolt1 properties individiually
print(bolt1.FullyBonded.getBoltDiameter())
print(bolt1.FullyBonded.getJointShear())
print(bolt1.FullyBonded.getPreTensioningForce())

#Bulk assignment of bolt2 properties
bolt2.setBoltName("Example Bolt 2")
bolt2.setBoltType(BoltTypes.END_ANCHORED)
bolt2.EndAnchored.setProperties(BoltModulusE=250000, OutofPlaneSpacing=1.2, TensileCapacity=0.2)

#Bulk retrieval of bolt2 properties
print(bolt2.EndAnchored.getProperties())

#Assignment of bolt3 properties
bolt3.setBoltName("Example Bolt 3")
bolt3.setBoltType(BoltTypes.QUEENS_CABLE)
bolt3.PlainStrandCable.setProperties(AddBulges=True, AddPullOutForce=True, PullOutForce=1)
#Consult setProperties method definition in documentation to determine properties available.
bolt3.PlainStrandCable.setBulgeLocations([10,20,30])

#Retrieval of bolt2 properties
print(bolt3.PlainStrandCable.getProperties())
#Not all functions are accesible through the getProperties method. 
#Consult getProperties method definition in documentation to determine properties available.
print(bolt3.PlainStrandCable.getBulgeLocations())

model.close()