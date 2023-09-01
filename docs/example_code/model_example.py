from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

boltList = model.getAllBoltProperties()
linerList = model.getAllLinerProperties()
jointList = model.getAllJointProperties()

bolt1 = model.getBoltPropertyByName("Bolt 1")
liner1 = model.getLinerPropertyByName("Liner 1")
joint1 = model.getJointPropertyByName("Joint 1")

model.save()
model.compute()
model.close()