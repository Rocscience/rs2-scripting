from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simpleProbabilistic.fez")
model.saveAndCompute()