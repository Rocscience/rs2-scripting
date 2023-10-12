from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import *
import Constants as constants

RS2Modeler.startApplication(constants.modelerPort, constants.modelerDebugPath)
modeler = RS2Modeler(port=constants.modelerPort)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

RS2Interpreter.startApplication(constants.interpreterPort, constants.interpreterDebugPath)
interpreter = RS2Interpreter(port=constants.interpreterPort)
interpreter.doNothing()