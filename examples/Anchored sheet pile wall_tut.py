from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os
import pandas as pd
import numpy as np

# Start RS2 Modeler and Interpreter
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open model
current_dir = os.path.dirname(os.path.abspath(__file__))
model = modeler.openFile(rf"{current_dir}\..\ExampleFiles\Anchored Sheet Pile Wall (Final)_default.fez")

# Material Properties
df_mat = pd.read_csv(rf"{current_dir}\..\ExampleFiles\material properties.csv") #read joints csv file
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
df_joint = pd.read_csv(rf"{current_dir}\..\ExampleFiles\joints.csv") #read joints csv file
joint1 = model.getAllJointProperties()[0] # get joint 1 properties

#Assigning joint1 properties individually
joint1.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB) # set slip criterion = mohr coulomb


# Liner Properties 
df_liner = pd.read_csv(rf"{current_dir}\..\ExampleFiles\liners.csv") #read liners csv file
liner1 = model.getAllLinerProperties()[0] # get liner 1 properties

#Assigning liner1 properties individually
liner1.setLinerName(df_liner.iat[0, 0]) #set liner 1 name
liner1.StandardBeam.setThickness(float(df_liner.iat[0,1])) #set liner thickness


# Bolt Properties 
df_bolt = pd.read_csv(rf"{current_dir}\..\ExampleFiles\bolts.csv") #read bolts csv file
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
model.saveAs(r"C:\Users\Public\Documents\Rocscience\RS2 Examples\Scripting\ExampleFiles\Anchored Sheet Pile Wall (Final)_import.fez")

# compute the new file
model.compute()

 
# Extract maximum displacement value on the wall

# Open RS2 Interpreter
RS2Interpreter.startApplication(port=60055)
interpreter = RS2Interpreter(port=60055)

# Open the new computed file
model_results = interpreter.openFile(r"C:\Users\Public\Documents\Rocscience\RS2 Examples\Scripting\ExampleFiles\Anchored Sheet Pile Wall (Final)_import.fez")

# Setting and retrieving results for solid total displacement
model_results.SetResultType(ExportResultType.SOLID_DISPLACEMENT_TOTAL_DISPLACEMENT)

# Add a material query line along the wall to model
points_making_line = [[10,8], [10,9], [10,10], [10,11], [10,12], [10,13], [10,14], [10,15], [10,16], [10,17], [10,18]]
lineID = model_results.AddMaterialQuery(points=points_making_line)

# Set model stage to desired stage number
model_results.SetActiveStage(4)

# Get results for material queries defined in your model
results = model_results.GetMaterialQueryResults()

# Extracting data for all material queries from model
for mat_query_data in results:
    unique_ID = mat_query_data.GetUniqueIdentifier()
    material_ID = mat_query_data.GetMaterialID()
    print(unique_ID, material_ID)
    print("------------------------")
    query_results = mat_query_data.GetAllValues()

    for result in query_results:
        print(type(result))
        x = result.GetXCoordinate()
        y = result.GetYCoordinate()
        distance = result.GetDistance()
        value = result.GetValue()
        print(x, y, distance, value)
