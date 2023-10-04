from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import *

RS2Modeler.startApplication(60057, r"C:\Users\WilliamSati\source\repos\RS2\RS2_2018\Build\Debug_x64\RS2.exe")
modeler = RS2Modeler(port=60057)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

RS2Interpreter.startApplication(60058, r"C:\Users\WilliamSati\source\repos\RS2\RS2_2018\Build\Debug_x64\Interpret.exe")
interpreter = RS2Interpreter(port=60058)
interpreter.doNothing()