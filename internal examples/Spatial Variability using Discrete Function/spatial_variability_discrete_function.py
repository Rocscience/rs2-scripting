from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *

import os

# Current folder location
current_dir = os.path.dirname(os.path.abspath(__file__)) 

# Output folder
output_dir = rf'{current_dir}\Results'
os.makedirs(output_dir, exist_ok=True)

# Output file path
output_file_name = 'Shear Strength Reduction Discrete Function Modified.fez'
output_path = os.path.join(output_dir, output_file_name)

# Start RS2 Modeler
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open model 
model = modeler.openFile(rf'{current_dir}\Shear Strength Reduction Discrete Function.fez')

# Modify properties by region by updating the cohesion and friction angle in the applied discrete function
# There are also ways to create a new function which can be found in the reference manual
df_name = "User Defined 1"
df1 = model.getDiscreteFunctionByName(df_name)
df_point_locations = df1.getPointLocations() #list of tuple[float,float]
df_phi = df1.getPointsPhi() #list of float values
for i in range(len(df_point_locations)):
    # modify values 
    if df_point_locations[i][1] < 36 and df_point_locations[i][1] > 34:
        df_phi[i] = 20

df1.setPointsPhi(df_phi)
 
# Save as a different name
model.saveAs(output_path)

# Compute model
model.compute()

# Open RS2 interpreter
RS2Interpreter.startApplication(port=60055)
interpreter = RS2Interpreter(port=60055)

# View results
model_results = interpreter.openFile(output_path)
model_results.getCriticalSRF()


