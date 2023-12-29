from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *
from rs2.PropertyEnums import *
import csv

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")
model.SetExportResultType(ExportResultType.SOLID_EFF_STRESS_SIGMA_Z_EFF)
exportResult1 = model.GetMeshResults()

with open('validateMeshResults.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in exportResult1:
        ordered_data = [data['x_coord'], data['y_coord'], data['value']]
        writer.writerow(ordered_data)


