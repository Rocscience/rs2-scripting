from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.InterpreterGraphEnums import *
from pprint import pprint

interpreter = RS2Interpreter()

def report(path) :
	interpreter_model = interpreter.openFile(path)
	print(interpreter_model.getCriticalSRF())
	pass

report(rf"C:\scriptingModels\testSSR.fez")
report(rf"C:\scriptingModels\srf_value_133.fez")
report(rf"C:\scriptingModels\srf_value_undefined.fez")



