from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *

import os
import pandas as pd
import matplotlib.pyplot as plt

'''
This script demonstrates how to generate multiple models with different bolt spacing for 
analyzing designs of an anchored sheet pile wall. In this script you have
control if you want to create models (create_new_models=True), analyze results (analyze_results=True) or both. 

For model creation: 
- tieback bolt spacing is varied for three cases and saved to new model files

For analysis:
- horizontal displacement along a created query line is outputted to an excel xlsx file
- horizontal displacement, axial force, shear force and bending moment diagrams over the depth of wall (liner) are generated
    and this data is outputted to a csv file as well as to png image files

NOTE: User is guided on how to install openpyxl library to the Rocsript Python environment to output to xlsx format
'''

# Current directory 
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create output folder
output_dir = rf'{current_dir}\Bolt Spacing Study'
os.makedirs(output_dir, exist_ok=True)

# Bolt spacing values to test
spacings = [1, 2, 3] # metres

# Create new model file paths: [s=1.fez, s=2.fez, s=3.fez]
new_model_paths = []
for spacing in spacings:
    filename = f's={spacing}m.fez'
    output_path = os.path.join(output_dir, filename)
    new_model_paths.append(output_path)

# Test Controls to conveniently modify a process without needing to run all processes
# You can also consider creating different functions for each process, which is handy for calling a process multiple times
create_new_models = True
analyze_results = True

# Modelling #################################################################################
if create_new_models:
    # Start RS2 Modeler
    RS2Modeler.startApplication(port=60054)
    modeler = RS2Modeler(port=60054)

    # Open model
    model = modeler.openFile(rf"{current_dir}\Anchored Sheet Pile Wall Parametric Study (Initial).fez")

    # Modify spacing and create new model, then extract data
    for test_num in range(len(spacings)):

        # Set new bolt spacing
        for bolt in model.getAllBoltProperties():
            bolt.Tieback.setOutofPlaneSpacing(spacings[test_num])

        # Create new model 
        model.saveAs(new_model_paths[test_num])

        # Compute model
        model.compute()

    # Open to view all new models
    for new_model_path in new_model_paths:
        model = modeler.openFile(new_model_path)


# Result Interpretation ####################################################################### 
if analyze_results:
    # Let's examine stage 5 results

    # Open RS2 Interpreter
    RS2Interpreter.startApplication(port=60055)
    interpreter = RS2Interpreter(port=60055)

    # Here is how you can store all opened model result files and use them multiple times
    all_model_results = [interpreter.openFile(new_model_path) for new_model_path in new_model_paths]

    # Analysis stage
    stage_number = 5
    
    # Results Part I: 
    # Extract horizontal displacement data at stage 5 along the sheet pile wall (material queries) 
    
    # Generate 11 evenly-spaced points from top to bottom of wall: (10,18) to (10,8)
    point_along_wall = [[10, 18 - i] for i in range(11)] 
    depths = [(18 - y) for [x, y] in point_along_wall]
    # Create an empty distionary for the material queries data frame
    mat_que_dict = {"Depth": depths}

    for test_num in range(len(all_model_results)):
        # Current model results file
        model_results = all_model_results[test_num]

        # Setting results to solid horizontal displacement
        model_results.SetResultType(ExportResultType.SOLID_DISPLACEMENT_HORIZONTAL_DISPLACEMENT)

        # Set model to stage 5
        model_results.SetActiveStage(stage_number)
        
        # Add a material query line along the wall
        query_along_wall_id = model_results.AddMaterialQuery(points=point_along_wall)

        # Get material query results for active stage 

        # Method 1: only one query line, so use index 0 (first and only query)
        query_results = model_results.GetMaterialQueryResults()[0]

        # Method 2: use the query unique id
        for material_query_results in model_results.GetMaterialQueryResults():
            if material_query_results.GetUniqueIdentifier() == query_along_wall_id:
                query_results = material_query_results
                break
        
        spacing = spacings[test_num]
        series_label = f"s = {spacing} m"
        mat_que_dict[series_label] = []
        for query_point in query_results.GetAllValues():
            # Add data to the dictionary
            mat_que_dict[series_label].append(query_point.GetValue())                                          

    # Convert the dictionary to data frame
    mat_que_df = pd.DataFrame(mat_que_dict) 

    # Save the data frame to a csv
    mat_que_df.to_csv(rf"{output_dir}\horiz disp to depth at stage 5.csv", index=False)

    # Results Part II: 
    # Extract and plot axial force, shear force, and bending moment results at stage 5 for the liner

    liner_results_dfs = [] # list of data frames to store liner results
    for model_results in all_model_results:
        # read liner axial force, shear force, and bending moment
        liner_results = model_results.GetLinerResults(stages =[stage_number]) # output liner results on stage 5

        all_stage_liner_results = liner_results[stage_number] # output a list of all liner results at stage 5
        
        stage_liner_results = all_stage_liner_results[0] # get the one and only liner in this model

        # Create a distionary for the data frame and fill with first node data
        liner_first_node = stage_liner_results.liner_element_results[0]
        liner_dict = {"Depth (m)":[18 - liner_first_node.start_y], # calculate depth from top of wall
                        "Horizontal Displacement (m)":[liner_first_node.displacement_x1],
                        "Axial Force (kN)":[liner_first_node.axial_force1],
                        "Shear Force (kN)":[liner_first_node.shear_force1],
                        "Bending Moment (kNm)":[liner_first_node.moment1]
                    }

        for liner_node in stage_liner_results.liner_element_results:
            # Add remaining data to the liner results dictionary
            liner_dict["Depth (m)"].append(18 - liner_node.end_y) # calculate depth from top of wall
            liner_dict["Horizontal Displacement (m)"].append(liner_node.displacement_x2)
            liner_dict["Axial Force (kN)"].append(liner_node.axial_force2)
            liner_dict["Shear Force (kN)"].append(liner_node.shear_force2)
            liner_dict["Bending Moment (kNm)"].append(liner_node.moment2)
            
        # Convert the dictionary to data frame
        liner_results_dfs.append(pd.DataFrame(liner_dict)) 


    # Uncomment to try using Pandas to save each case as a tab in excel as a xls file, 
    # Remember to install openpyxl! 
    #   Open RS2 application: Scripting > Manage Python Environment 
    #   Type "pip install openpyxl" and hit Enter
    # To uninstall, repeat the above steps, but type "pip uninstall openpyxl"
    '''
    with pd.ExcelWriter(rf"{output_dir}\liner results at stage 5.xlsx") as writer:
        for test_num in range(len(liner_results_dfs)):
            liner_results_dfs[test_num].to_excel(writer, sheet_name=f"s = {spacings[test_num]} m", index=False)
    '''

    # Using Matplotlib library to plot data

    # define a function to format plot
    def format_plot():
        plt.gca().spines['bottom'].set_position(('data',0)) # move x-axis to y=0
        plt.gca().xaxis.set_label_position('top') # set x-axis label position to the top
        plt.gca().invert_yaxis() # invert y-axis
        plt.gca().spines['left'].set_position(('data',0)) # move y-axis to x=0
        plt.gca().spines['top'].set_visible(False) # hide the top spine
        plt.gca().spines['right'].set_visible(False) # hide the right spine

    # Plot Liner Horizontal Displacement
    plt.figure()
    plt.xlabel("Horizontal Displacement (m)")
    plt.ylabel("Depth (m)")
    plt.title("Liner Horizontal Displacement at Stage 5")
    for test_num in range(len(liner_results_dfs)):
        liner_results_df = liner_results_dfs[test_num]
        plt.plot(liner_results_df["Horizontal Displacement (m)"], liner_results_df["Depth (m)"], label=f"s = {spacings[test_num]} m")

    # format plot display
    plt.legend()
    format_plot()
    plt.gca().yaxis.set_label_position('right') # set y-axis label position to the right
    plt.gca().spines['left'].set_position(('data',-0.03)) # move y-axis to x=-0.03
    # save plot
    plt.savefig(rf"{output_dir}\liner horizontal displacement at stage 5.png")


    # Plot Liner Axial Force
    plt.figure()
    plt.xlabel("Axial Force (kN)")
    plt.ylabel("Depth (m)")
    plt.title("Liner Axial Force at Stage 5")
    for test_num in range(len(liner_results_dfs)):
        liner_results_df = liner_results_dfs[test_num]
        plt.plot(liner_results_df["Axial Force (kN)"], liner_results_df["Depth (m)"], label=f"s = {spacings[test_num]} m")

    # format plot display
    plt.legend()
    format_plot()
    plt.gca().yaxis.set_label_position('left') # set y-axis label position to the left
    # save plot
    plt.savefig(rf"{output_dir}\liner axial force at stage 5.png")


    # Plot Liner Shear Force Diagram
    plt.figure()
    plt.xlabel("Shear Force (kN)")
    plt.ylabel("Depth (m)")
    plt.title("Liner Shear Force at Stage 5")
    for test_num in range(len(liner_results_dfs)):
        liner_results_df = liner_results_dfs[test_num]
        plt.plot(liner_results_df["Shear Force (kN)"], liner_results_df["Depth (m)"], label=f"s = {spacings[test_num]} m")

    # format plot display
    plt.legend()
    format_plot()
    plt.gca().yaxis.set_label_position('right')
    # save plot
    plt.savefig(rf"{output_dir}\liner shear force at stage 5.png")


    # Plot Liner Bending Moment
    plt.figure()
    plt.xlabel("Bending Moment (kNm)")
    plt.ylabel("Depth (m)")
    plt.title("Liner Bending Moment at Stage 5")
    # Extract data for Liner Bending Moment Diagram
    for test_num in range(len(liner_results_dfs)):
        liner_results_df = liner_results_dfs[test_num]
        plt.plot(liner_results_df["Bending Moment (kNm)"], liner_results_df["Depth (m)"], label=f"s = {spacings[test_num]} m")

    # format plot display
    plt.legend()
    format_plot()
    plt.gca().yaxis.set_label_position('right') 
    # save plot
    plt.savefig(rf"{output_dir}\liner bending moment at stage 5.png")

    plt.show()
    # close the figure windows to finish the script

