from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\example_rs2_file.fez")

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]

bolt1.setBoltType(BoltTypes.FULLY_BONDED)
print(bolt1.getBoltType())

