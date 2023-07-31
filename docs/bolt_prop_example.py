from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\example_rs2_file.fez")

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]

bolt1.setBoltType(bolt1.BoltTypes.FULLY_BONDED)
print(bolt1.getBoltType())

bolt1.setBoltDiameter(23)
print(bolt1.getBoltDiameter())

bolt1.setBoltModulusE(201000)
print(bolt1.getBoltModulusE())

bolt1.setTensileCapacity(0.2)
print(bolt1.getTensileCapacity())

bolt1.setResidualTensileCapacity(0.1)
print(bolt1.getResidualTensileCapacity())

bolt1.setOutofPlaneSpacing(1.5)
print(bolt1.getOutofPlaneSpacing())

bolt1.setPreTensioningForce(1)
print(bolt1.getPreTensioningForce())

bolt1.setConstantPretensioningForceInInstallStage(False)
print(bolt1.getConstantPretensioningForceInInstallStage())

bolt1.setJointShear(True)
print(bolt1.getJointShear())