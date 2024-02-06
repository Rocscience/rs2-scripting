from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltPropertyByName("Bolt 2")
print(bolt.getBoltType())

interpreter = RS2Interpreter()
interpreter.doNothing()

