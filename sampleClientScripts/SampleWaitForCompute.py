from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltByName("Bolt 2")

for i in range(10):
	bolt.setBoltDiameter(23 + i)
	model.saveAndCompute()