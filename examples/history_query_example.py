from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *

import pandas as pd
import matplotlib.pyplot as plt
import os

# Current folder location
current_dir = os.path.dirname(os.path.abspath(__file__))

# Output folder
output_dir = rf'{current_dir}\history_query_example'
os.makedirs(output_dir, exist_ok=True)

# Output file path
output_file_name = 'Embankment Consolidation - History Query.fez'
output_path = os.path.join(output_dir, output_file_name)


# Add history node to model

# Start RS2 Modeler
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open model 
model = modeler.openFile(rf"C:\Users\Public\Documents\Rocscience\RS2 Examples\Tutorials\Consolidation Settlement\Embankment Consolidation.fez")

# Save as a different name
model.saveAs(output_path)

# Add a history query
model.AddHistoryQueryPoint(x=55,y=-10,history_query_name='HQ 1')

# Compute model
model.compute()


# Extract excess pore pressure history from start of stage 2 to end of model

# Open RS2 interpreter
RS2Interpreter.startApplication(port=60055)
interpreter = RS2Interpreter(port=60055)

# Extract data
stage_indices = range(2,9) #stage 2 to 8
model_results = interpreter.openFile(output_path)
excess_pore_pressure_time_history_all_stages = model_results.GetHistoryQueryResults('HQ 1', 
                                     HistoryQueryGraphEnums.HorizontalAxisTypes.TIME, 
                                     HistoryQueryGraphEnums.VerticalAxisTypes.PORE_PRESSURE, 
                                     stage_indices)

# Create dataframe
time_label = 'Time (d)'
excess_pore_pressure_label = 'Excess Pore Pressure (kPa)'
data_for_dataFrame = []
for stage_data in excess_pore_pressure_time_history_all_stages.values():
    for history_query_point in stage_data:
        # Append the data to the list
        data_for_dataFrame.append([history_query_point.GetHorizontalAxisResult(), history_query_point.GetVerticalAxisResult()])

df_epp = pd.DataFrame(data_for_dataFrame, columns=[time_label, excess_pore_pressure_label])

# Calculate excess pore pressure using the end of stage 1 (start of stage 2) as the reference stage
reference_pore_pressure = df_epp[excess_pore_pressure_label].iloc[0]
df_epp[excess_pore_pressure_label] = df_epp[excess_pore_pressure_label] - reference_pore_pressure

# Export data
df_epp.to_csv(os.path.join(output_dir, 'Embankment Consolidation - History Query.csv'), index=False)

# Plot data
plt.plot(df_epp[time_label], df_epp[excess_pore_pressure_label])

plt.xlabel(time_label)
plt.ylabel(excess_pore_pressure_label)
plt.title('Excess Pore Pressure History')

plt.show()


