from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Start RS2 Modeler and Interpreter
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Current directory 
current_dir = os.path.dirname(os.path.abspath(__file__))

# Output directory
output_dir = rf"{current_dir}\results"
os.makedirs(output_dir, exist_ok=True)

# Open model
model = modeler.openFile(rf"{current_dir}\Anchored Sheet Pile Wall_scripting (Initial).fez")

# Material Properties
df_mat = pd.read_csv(rf"{current_dir}\material properties.csv") #read material properties csv file 
material1 = model.getAllMaterialProperties()[0] # get material 1 properties
material2 = model.getAllMaterialProperties()[1] # get material 2 properties

# Assigning material 1 properties individually
material1.InitialConditions.setUnitWeight(float(df_mat.iat[0, 1])) # set unit wetight
material1.Stiffness.Isotropic.setPoissonsRatio(float(df_mat.iat[0, 2])) # set poissons ratio
material1.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC) # set material type to plastic
material1.Strength.MohrCoulombStrength.setPeakCohesion(float(df_mat.iat[0, 7])) # set peak cohesion
material1.Strength.MohrCoulombStrength.setResidualCohesion(float(df_mat.iat[0, 9])) # set residual cohesion

# Assigning material 2 properties individually
material2.setMaterialName(df_mat.iat[1, 0]) # set material name
material2.InitialConditions.setUnitWeight(float(df_mat.iat[1, 1])) # set unit wetight
material2.Stiffness.Isotropic.setPoissonsRatio(float(df_mat.iat[1, 2])) # set poissons ratio
material2.Stiffness.Isotropic.setYoungsModulus(float(df_mat.iat[1, 3])) # set youngs modulus
material2.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC) # set material type to plastic
material2.Strength.MohrCoulombStrength.setPeakFrictionAngle(float(df_mat.iat[1, 6])) # set peak friction angle
material2.Strength.MohrCoulombStrength.setPeakCohesion(float(df_mat.iat[1, 7])) # set peak cohesion
material2.Strength.MohrCoulombStrength.setResidualFrictionAngle(float(df_mat.iat[1, 8])) # set residual friction angle
material2.Strength.MohrCoulombStrength.setResidualCohesion(float(df_mat.iat[1, 9])) # set residual cohesion 

# Joint Properties
df_joint = pd.read_csv(rf"{current_dir}\joints.csv") #read joints csv file 
joint1 = model.getAllJointProperties()[0] # get joint 1 properties

#Assigning joint1 properties individually
joint1.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB) # set slip criterion = mohr coulomb

# Liner Properties 
df_liner = pd.read_csv(rf"{current_dir}\liners.csv") #read liners csv file
liner1 = model.getAllLinerProperties()[0] # get liner 1 properties

#Assigning liner1 properties individually
liner1.setLinerName(df_liner.iat[0, 0]) #set liner 1 name
liner1.StandardBeam.setThickness(float(df_liner.iat[0,1])) #set liner thickness


# Bolt Properties 
df_bolt = pd.read_csv(rf"{current_dir}\bolts.csv") #read bolts csv file 
boltList = model.getAllBoltProperties()

# get/set bolt properties for each bolt
for index, read_bolt_props in df_bolt.iterrows(): 
    bolt_props = boltList[index] # get the bolt properties of the current row index

    # reformat Type column value
    bolt_props.setBoltType(BoltTypes.TIEBACK_BOLT) # set bolt type = Tieback

    # read and set bolt properties for each bolt
    bolt_props.Tieback.setBondShearStiffness(float(df_bolt.iat[index,2])) # set'Bond Shear Stiffness'
    bolt_props.Tieback.setBondStrength(float(df_bolt.iat[index, 3])) # set 'Bond Strength'
    bolt_props.Tieback.setBoreholeDiameter(float(df_bolt.iat[index, 4])) # set'Borehole Diameter'
    bolt_props.Tieback.setPreTensioningForce(float(df_bolt.iat[index, 5])) # set 'Pre-Tensioning Force'
    bolt_props.Tieback.setPercentageBondLength(int(df_bolt.iat[index, 6])) # set 'Percentage Bond Length'

# Save the modeler file as a new file
model.saveAs(rf"{output_dir}\Anchored Sheet Pile Wall_scripting (Final).fez") # test

# compute the new file
model.compute()

# Extract displacement value on the wall

# Open RS2 Interpreter
RS2Interpreter.startApplication(port=60055)
interpreter = RS2Interpreter(port=60055)

# Open the new computed file
model_results = interpreter.openFile(rf"{output_dir}\Anchored Sheet Pile Wall_scripting (Final).fez")

# Results Part I: 
# Extract total displacement data at stage 4 along the sheet pile wall (material queries)

# Setting results to solid total displacement
model_results.SetResultType(ExportResultType.SOLID_DISPLACEMENT_TOTAL_DISPLACEMENT)

# Add a material query line along the wall
points_making_line = [[10, 8 + i] for i in range(11)] # Generate 11 evenly-spaced points from coordinates (10,8) to (10,18)
lineID = model_results.AddMaterialQuery(points=points_making_line)

# Set model to stage 4
model_results.SetActiveStage(4)

# Get material queries results at stage 4
query_results = model_results.GetMaterialQueryResults()[0] # get the material query results at stage 4:
                                                                # GetMaterialQueryResults() returns a list grouped by stages, since there is a defined active stage,
                                                                # it is the only item contained in the list. Therefore GetMaterialQueryResults()[0]


# Create an empty distionary for the material queries data frame
mat_que_dict = {"X":[], "Y":[],"Distance":[], "Total Displacement (m)":[]}


# Extracting data for material queries
for query_point in query_results.GetAllValues():
    x = query_point.GetXCoordinate()
    y = query_point.GetYCoordinate()
    distance = query_point.GetDistance()
    value = query_point.GetValue()

    # Add data to the dictionary
    mat_que_dict["X"].append(x)
    mat_que_dict["Y"].append(y)
    mat_que_dict["Distance"].append(distance)
    mat_que_dict["Total Displacement (m)"].append(value)

# Output results to a new csv

# Convert the dictionary to data frame
mat_que_df = pd.DataFrame(mat_que_dict) 

# Save the data frame to a csv
mat_que_df.to_csv(rf"{output_dir}\material queries_total disp at stage 4.csv", index=False)

# Results Part II: 
# Extract and plot axial force, shear force, and bending moment results at stage 5 for the liner

# read liner axial force, shear force, and bending moment
stage_number = 5
liner_results = model_results.GetLinerResults(stages =[stage_number]) # output liner results on stage 5

stage_liner_results = liner_results[stage_number][0] #output the first liner results at stage 5

# Create an empty distionary for the data frame
liner_dict = {"Start Node":[], "End Node":[],"Start Node X":[], "Start Node Y":[], 
                "End Node X":[], "End Node Y":[], "Distance (m)":[], "Axial Force (kN)":[],
                "Shear Force (kN)":[], "Bending Moment_start (kNm)":[], "Bending Moment_mid (kNm)":[],
                "Bending Moment_end (kNm)":[]}

for liner_node in stage_liner_results.liner_element_results:
    # output axial force, shear force, and bending moment for each node
    node_start = liner_node.node_start
    node_end = liner_node.node_end
    start_x = liner_node.start_x
    start_y = liner_node.start_y
    end_x = liner_node.end_x
    end_y = liner_node.end_y
    distance = liner_node.distance

    axial_force = liner_node.axial_force
    shear_force = liner_node.shear_force
    moment1 = liner_node.moment1
    moment_mid = liner_node.moment_mid
    moment2 = liner_node.moment2

    # Add data to the liner results dictionary
    liner_dict["Start Node"].append(node_start)
    liner_dict["End Node"].append(node_end)
    liner_dict["Start Node X"].append(start_x)
    liner_dict["Start Node Y"].append(start_y)
    liner_dict["End Node X"].append(end_x)
    liner_dict["End Node Y"].append(end_y)
    liner_dict["Distance (m)"].append(distance)
    liner_dict["Axial Force (kN)"].append(axial_force)
    liner_dict["Shear Force (kN)"].append(shear_force)
    liner_dict["Bending Moment_start (kNm)"].append(moment1)
    liner_dict["Bending Moment_mid (kNm)"].append(moment_mid)
    liner_dict["Bending Moment_end (kNm)"].append(moment2)

# Convert the dictionary to data frame
liner_results_df = pd.DataFrame(liner_dict) 

# Save the data frame to a csv
liner_results_df.to_csv(rf"{output_dir}\liner results at stage 5.csv", index=False)

# Plot Liner Axial Force
plt.figure()
plt.plot(liner_results_df["Distance (m)"], liner_results_df["Axial Force (kN)"])

plt.xlabel("Distance (m)")
plt.ylabel("Axial Force (kN)")
plt.title("Liner Axial Force_stage 5")

plt.savefig(rf"{output_dir}\liner axial force_stage 5.png")

# Plot Liner Shear Force
plt.figure()
plt.plot(liner_results_df["Distance (m)"], liner_results_df["Shear Force (kN)"])

plt.xlabel("Distance (m)")
plt.ylabel("Shear Force (kN)")
plt.title("Liner Shear Force_stage 5")

plt.savefig(rf"{output_dir}\liner shear force_stage 5.png")

# Extract data for Liner Bending Moment graph

moment_dist = [] # x-axis data
moment_value = [] # y-axis data

distance_col = liner_results_df["Distance (m)"]
moment1_col = liner_results_df["Bending Moment_start (kNm)"]
moment_mid_col = liner_results_df["Bending Moment_mid (kNm)"]
moment2_col = liner_results_df["Bending Moment_end (kNm)"]


for index in distance_col.index:

    if index == distance_col.index.min():
        moment_dist.append(0)
        moment_dist.append(distance_col[index])

    elif index != distance_col.index.min() and index!= distance_col.index.max():
        moment_dist.append((distance_col[index] + distance_col[index-1])/2)
        moment_dist.append(distance_col[index])

    elif index == distance_col.index.max():
        moment_dist.append((distance_col[index] + distance_col[index-1])/2)
        moment_dist.append(distance_col[index])
        gap = distance_col[index] - distance_col[index-1]
        moment_dist.append(distance_col[index] + gap)


for index in moment1_col.index:

    if index != moment1_col.index.max():
        moment_value.append(moment1_col[index])
        moment_value.append(moment_mid_col[index])

    elif index == moment1_col.index.max():
        moment_value.append(moment1_col[index])
        moment_value.append(moment_mid_col[index])
        moment_value.append(moment2_col[index])

# Plot Liner Bending Moment
plt.figure()
plt.plot(moment_dist, moment_value)

plt.xlabel("Distance (m)")
plt.ylabel("Bending Moment (kNm)")
plt.title("Liner Bending Moment_stage 5")

plt.savefig(rf"{output_dir}\liner bending moment_stage 5.png")

plt.show()
# close the figure windows to finish the script

