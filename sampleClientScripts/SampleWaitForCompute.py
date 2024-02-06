from rs2.modeler.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltPropertyByName("Bolt 2")

for i in range(10):
	bolt.FullyBonded.setBoltDiameter(23 + i)
	model.compute()