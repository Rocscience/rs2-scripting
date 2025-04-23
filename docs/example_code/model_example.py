from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60077)
modeler = RS2Modeler(port=60077)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

bolt = model.getAllBoltProperties()[0]
liner = model.getAllLinerProperties()[0]
joint = model.getAllJointProperties()[0]

bolt.setBoltType(BoltTypes.SWELLEX)
liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
joint.setSlipCriterion(JointTypes.MATERIAL_DEPENDENT)

model.save()
model.compute()
model.close()

RS2Interpreter.startApplication(port=60078)
interpreter = RS2Interpreter(port=60078)
interpreterModel = interpreter.openFile(rf"{current_dir}\example_models\ExampleModel.fez")
interpreterModel.save()
interpreterModel.close()

modeler.closeProgram()
interpreter.closeProgram()