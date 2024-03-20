from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
import os, inspect
from pprint import pprint

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None)))

# Get Units for Interpreter
interpreter = RS2Interpreter()
interpreterModel = interpreter.openFile(rf"{current_dir}\example_models\SupportResults.fez")
interpreterModelUnits = interpreterModel.getUnits()

print("\nInterpreter Model Units")
print("\nSolid Units :")
pprint(interpreterModelUnits.solid_units)
print("\nHydro Units :")
pprint(interpreterModelUnits.hydro_units)
print("\nThermal Units :")
pprint(interpreterModelUnits.thermal_units)

# Get Units for Modeler
modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\SupportStructuralResults.fez")
modelerUnits = model.getUnits()

print("\nModeler Units")
print("\nSolid Units :")
pprint(modelerUnits.solid_units)
print("\nHydro Units :")
pprint(modelerUnits.hydro_units)
print("\nThermal Units :")
pprint(modelerUnits.thermal_units)

# Reset Properties for model
model.ResetProperties()

# Close the models
model.close()
interpreterModel.close()
