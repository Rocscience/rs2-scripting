from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import *

modelerPortToUse = 60054
interpreterPortToUse = 60055

RS2Modeler.startApplication(modelerPortToUse)
modeler = RS2Modeler(port=modelerPortToUse)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

RS2Interpreter.startApplication(interpreterPortToUse)
interpreter = RS2Interpreter(port=interpreterPortToUse)
interpreter.doNothing()