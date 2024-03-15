from rs2.modeler.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simpleProbabilistic.fez")
model.save()
model.compute()