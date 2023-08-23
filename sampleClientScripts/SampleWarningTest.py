from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_computation_warning.fez")
model.saveAndCompute()
