from rs2.modeler.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model1 = modeler.openFile(r'C:\Users\WilliamSati\Downloads\queryPointTest.fez')
bolt1 = model1.getFirstBolt()
bolt1.setBoltName("thisIsModel1")

model2 = modeler.openFile(r'C:\Intel\simple_3_stage.fez')
bolt2 = model2.getFirstBolt()
bolt2.setBoltName("thisIsModel2")

#try to set something back in model1 now that the view is focused on model2...
bolt1.setBoltType(bolt1.BoltTypes.FULLY_BONDED)
print(bolt1.getBoltType())

#try to set something back in model2
bolt2.setBoltType(bolt1.BoltTypes.FULLY_BONDED)
print(bolt2.getBoltType())

#set remaining properties, alternating between model 1 and 2
bolt1.setBoltDiameter(21)
print(bolt1.getBoltDiameter())
bolt2.setBoltDiameter(22)
print(bolt2.getBoltDiameter())

bolt1.setBoltModuluse(201000)
print(bolt1.getBoltModuluse())
bolt2.setBoltModuluse(202000)
print(bolt2.getBoltModuluse())

bolt1.setTensileCapacity(0.1)
print(bolt1.getTensileCapacity())
bolt2.setTensileCapacity(0.2)
print(bolt2.getTensileCapacity())

bolt1.setResidualTensileCapacity(0.01)
print(bolt1.getResidualTensileCapacity())
bolt2.setResidualTensileCapacity(0.02)
print(bolt2.getResidualTensileCapacity())

bolt1.setOutofplaneSpacing(1)
print(bolt1.getOutofplaneSpacing())
bolt2.setOutofplaneSpacing(2)
print(bolt2.getOutofplaneSpacing())

bolt1.setPretensioningForce(1)
print(bolt1.getPretensioningForce())
bolt2.setPretensioningForce(2)
print(bolt2.getPretensioningForce())

bolt1.setConstantPretensioningForceInInstallStage(False)
print(bolt1.getConstantPretensioningForceInInstallStage())
bolt2.setConstantPretensioningForceInInstallStage(False)
print(bolt2.getConstantPretensioningForceInInstallStage())

bolt1.setJointShear(False)
print(bolt1.getJointShear())
bolt2.setJointShear(False)
print(bolt2.getJointShear())

model1.saveAs(r'C:\Users\WilliamSati\Downloads\queryPointTest2.fez')
model2.saveAs(r'C:\Users\WilliamSati\Downloads\simple_3_stage2.fez')
model1.saveAndCompute()
model2.saveAndCompute()

#try closing only one of the models. 
model2.close()
