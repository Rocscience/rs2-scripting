from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

boltList = model.getAllBoltProperties()
linerList = model.getAllLinerProperties()
jointList = model.getAllJointProperties()

bolt1 = model.getBoltPropertyByName("Test Bolt 1")
liner1 = model.getLinerPropertyByName("Test Liner 1")
joint1 = model.getJointPropertyByName("Test Joint 1")

for bolt in range(3):
	boltName = "Bolt " + str(bolt + 1)
	boltList[bolt].setBoltName(boltName)

for liner in range(3):
	linerName = "Liner " + str(liner + 1)
	linerList[liner].setLinerName(linerName)

for joint in range(3):
	jointName = "Joint " + str(joint + 1)
	jointList[joint].setJointName(jointName)

model.save()
model.compute()
model.close()