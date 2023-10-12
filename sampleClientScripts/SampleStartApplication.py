from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import *
import Paths as paths

RS2Modeler.startApplication(60057, paths.modelerDebugPath)
modeler = RS2Modeler(port=60057)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

RS2Interpreter.startApplication(60058, paths.interpreterDebugPath)
interpreter = RS2Interpreter(port=60058)
interpreter.doNothing()