from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\example_rs2_file.fez")

boltList = model.getAllBoltProperties()
linerList = model.getAllLinerProperties()

bolt1 = model.getBoltPropertyByName("Bolt 1")
liner1 = model.getLinerPropertyByName("Liner 1")

model.save(r"C:\example_rs2_file2.fez")
model.saveAndCompute()
model.close()