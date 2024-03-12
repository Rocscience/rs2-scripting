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
output_dir = rf'{current_dir}\Results'
os.makedirs(output_dir, exist_ok=True)

# Output file path
output_file_name = 'Embankment Consolidation (History Queries).fez'
output_path = os.path.join(output_dir, output_file_name)

# Add history node to model

# Start RS2 Modeler
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open model 
model = modeler.openFile(rf'{current_dir}\Embankment Consolidation (Initial).fez')

# Save as a different name
model.saveAs(output_path)

# Add history queries
history_query_names = ['HQ 1', 'HQ 2', 'HQ 3', 'HQ 4', 'HQ 5']
model.AddHistoryQueryPoint(x=35,y=-8,history_query_name=history_query_names[0])
model.AddHistoryQueryPoint(x=45,y=-9,history_query_name=history_query_names[1])
model.AddHistoryQueryPoint(x=55,y=-10,history_query_name=history_query_names[2])
model.AddHistoryQueryPoint(x=65,y=-11,history_query_name=history_query_names[3])
model.AddHistoryQueryPoint(x=75,y=-12,history_query_name=history_query_names[4])

# Compute model
model.compute()

# Extract excess pore pressure history from start of stage 2 to end of model

# Open RS2 interpreter
RS2Interpreter.startApplication(port=60055)
interpreter = RS2Interpreter(port=60055)

# Analyze Excess Pore Pressure History
stage_indices = range(2,9) #stage 2 to 8
model_results = interpreter.openFile(output_path)
time_label = 'Time (d)'
excess_pore_pressure_label = 'Excess Pore Pressure (kPa)'

for history_query_name in history_query_names:
    # Extract data
    excess_pore_pressure_time_history_all_stages = model_results.GetHistoryQueryResults(f'{history_query_name}', 
                                        HistoryQueryGraphEnums.HorizontalAxisTypes.TIME, 
                                        HistoryQueryGraphEnums.VerticalAxisTypes.PORE_PRESSURE, 
                                        stage_indices)

    # Create dataframe
    data_for_dataframe = []
    for stage_data in excess_pore_pressure_time_history_all_stages.values():
        for history_query_point in stage_data:
            # Append the data to the list
            data_for_dataframe.append([history_query_point.GetHorizontalAxisResult(), history_query_point.GetVerticalAxisResult()])

    df_epp = pd.DataFrame(data_for_dataframe, columns=[time_label, excess_pore_pressure_label])

    # Calculate excess pore pressure using the end of stage 1 (start of stage 2) as the reference stage
    reference_pore_pressure = df_epp[excess_pore_pressure_label].iloc[0]
    df_epp[excess_pore_pressure_label] = df_epp[excess_pore_pressure_label] - reference_pore_pressure

    # Export data
    df_epp.to_csv(os.path.join(output_dir, rf'{history_query_name}.csv'), index=False)

    # Plot data
    plt.plot(df_epp[time_label], df_epp[excess_pore_pressure_label], label = rf'{history_query_name}')

# Save plot
plt.xlabel(time_label)
plt.ylabel(excess_pore_pressure_label)
plt.title('Excess Pore Pressure History')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Excess Pore Pressure History.png'))

# Uncomment the following line to show the plot on the screen
#plt.show()



