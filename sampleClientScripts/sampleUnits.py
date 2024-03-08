
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter

interpret = RS2Interpreter()
model2 = interpret.openFile(r"C:\scriptingModels\joint.fez")
units2 = model2.getUnits()



modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\si.fez")
units = model.getUnits()
model.ResetProperties()
model.close()

pass
