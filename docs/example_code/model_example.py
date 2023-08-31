from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

boltList = model.getAllBoltProperties()
linerList = model.getAllLinerProperties()

bolt1 = model.getBoltPropertyByName("Test Bolt 1")
liner1 = model.getLinerPropertyByName("Test Liner 1")

model.save()
model.compute()
model.close()