from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\example_rs2_file.fez")

bolt = model.getBoltPropertyByName("Bolt 1")

bolt.setBoltType(bolt.BoltTypes.FULLY_BONDED)
print(bolt.getBoltType())

bolt.setBoltDiameter(23)
print(bolt.getBoltDiameter())

bolt.setBoltModulusE(201000)
print(bolt.getBoltModulusE())

bolt.setTensileCapacity(0.2)
print(bolt.getTensileCapacity())

bolt.setResidualTensileCapacity(0.1)
print(bolt.getResidualTensileCapacity())

bolt.setOutofPlaneSpacing(1.5)
print(bolt.getOutofPlaneSpacing())

bolt.setPreTensioningForce(1)
print(bolt.getPreTensioningForce())

bolt.setConstantPretensioningForceInInstallStage(False)
print(bolt.getConstantPretensioningForceInInstallStage())

bolt.setJointShear(True)
print(bolt.setJointShear())