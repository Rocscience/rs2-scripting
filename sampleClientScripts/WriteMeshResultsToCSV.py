from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.modeler.properties.PropertyEnums import *
import csv

interpreter = RS2Interpreter()
model = interpreter.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
model.SetResultType(ExportResultType.SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z)
exportResult1 = model.GetMeshResults()

with open('validateMeshResults.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in exportResult1:
        ordered_data = [data['x_coord'], data['y_coord'], data['value']]
        writer.writerow(ordered_data)


