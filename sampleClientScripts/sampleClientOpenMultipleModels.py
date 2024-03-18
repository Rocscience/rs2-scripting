from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model1 = modeler.openFile(r'C:\Users\WilliamSati\Downloads\queryPointTest.fez')
bolt1 = model1.getAllBoltProperties()[0]
bolt1.setBoltName("thisIsModel1")

model2 = modeler.openFile(r'C:\Intel\simple_3_stage.fez')
bolt2 = model2.getAllBoltProperties()[0]
bolt2.setBoltName("thisIsModel2")

#try to set something back in model1 now that the view is focused on model2...
bolt1.setBoltType(BoltTypes.FULLY_BONDED)
print(bolt1.getBoltType())

#try to set something back in model2
bolt2.setBoltType(BoltTypes.FULLY_BONDED)
print(bolt2.getBoltType())

#set remaining properties, alternating between model 1 and 2
bolt1.FullyBonded.setBoltDiameter(21)
print(bolt1.FullyBonded.getBoltDiameter())
bolt2.FullyBonded.setBoltDiameter(22)
print(bolt2.FullyBonded.getBoltDiameter())

bolt1.FullyBonded.setBoltModulusE(201000)
print(bolt1.FullyBonded.getBoltModulusE())
bolt2.FullyBonded.setBoltModulusE(202000)
print(bolt2.FullyBonded.getBoltModulusE())

bolt1.FullyBonded.setTensileCapacity(0.1)
print(bolt1.FullyBonded.getTensileCapacity())
bolt2.FullyBonded.setTensileCapacity(0.2)
print(bolt2.FullyBonded.getTensileCapacity())

bolt1.FullyBonded.setResidualTensileCapacity(0.01)
print(bolt1.FullyBonded.getResidualTensileCapacity())
bolt2.FullyBonded.setResidualTensileCapacity(0.02)
print(bolt2.FullyBonded.getResidualTensileCapacity())

bolt1.FullyBonded.setOutofPlaneSpacing(1)
print(bolt1.FullyBonded.getOutofPlaneSpacing())
bolt2.FullyBonded.setOutofPlaneSpacing(2)
print(bolt2.FullyBonded.getOutofPlaneSpacing())

bolt1.FullyBonded.setPreTensioningForce(1)
print(bolt1.FullyBonded.getPreTensioningForce())
bolt2.FullyBonded.setPreTensioningForce(2)
print(bolt2.FullyBonded.getPreTensioningForce())

bolt1.FullyBonded.setConstantPretensioningForceInInstallStage(False)
print(bolt1.FullyBonded.getConstantPretensioningForceInInstallStage())
bolt2.FullyBonded.setConstantPretensioningForceInInstallStage(False)
print(bolt2.FullyBonded.getConstantPretensioningForceInInstallStage())

bolt1.FullyBonded.setJointShear(False)
print(bolt1.FullyBonded.getJointShear())
bolt2.FullyBonded.setJointShear(False)
print(bolt2.FullyBonded.getJointShear())

model1.saveAs(r'C:\Users\WilliamSati\Downloads\queryPointTest2.fez')
model2.saveAs(r'C:\Users\WilliamSati\Downloads\simple_3_stage2.fez')

model1.save()
model1.compute()

model2.save()
model2.compute

#try closing only one of the models. 
model2.close()
