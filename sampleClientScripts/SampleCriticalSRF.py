from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.InterpreterGraphEnums import *
from pprint import pprint
import numpy as np
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *


modeler = RS2Modeler()
interpreter = RS2Interpreter()

path = r"C:\scriptingModels\srf_value_133.fez"
model =  modeler.openFile(path)

mat = model.getAllMaterialProperties()[0]


mat.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BODY_FORCE_ONLY)
mat.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
mat.InitialConditions.setUnitWeight(1000)  
mat.InitialConditions.setPorosityValue(0.5)
srf_values = []
porosity_stdev = 0.005
unit_weight_stdev = 100  

for i in range(10):

	porosity = np.random.normal(loc=0.5, scale=porosity_stdev)
	unit_weight = np.random.normal(loc=1000, scale=unit_weight_stdev)

	mat.InitialConditions.setPorosityValue(porosity)
	mat.InitialConditions.setUnitWeight( i * 1000)
	model.save()
	model.compute()
	interpreter_model = interpreter.openFile(path)
	srf_values.append(interpreter_model.getCriticalSRF())
	interpreter_model.close()

pass




def report(path) :
	interpreter_model = interpreter.openFile(path)
	print(interpreter_model.getCriticalSRF())
	pass

report(rf"C:\scriptingModels\testSSR.fez")
report(rf"C:\scriptingModels\srf_value_133.fez")
report(rf"C:\scriptingModels\srf_value_undefined.fez")



