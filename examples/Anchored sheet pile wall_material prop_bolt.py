from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os
import pandas as pd
import numpy as np

# Start RS2 Modeler and Interpreter
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open model
current_dir = os.path.dirname(os.path.abspath(__file__))
model = modeler.openFile(rf"{current_dir}\..\ExampleFiles\Anchored Sheet Pile Wall (Final)_default.fez")


# Reformat type function: reformat support type names based on similarity and returns support type string
def reformat_type(type_name: str):
    type_lower = type_name.lower()

    # Ex. Mohr Coloumb or MC will get correct str JJOINT_MOHR_COULOMB
    #     Tieback or Tie back will get correct str TIEBACK_BOLT
    if ('mohr' in type_lower and 'coloumb' in type_lower) or ('m' in type_lower and 'c' in type_lower):
        type_str = 'JOINT_MOHR_COULOMB' 
    elif 'tie' in type_lower and 'back' in type_lower:
        type_str = 'TIEBACK_BOLT'
    else:
        raise ValueError(f"Type name '{type_name}' cannot be identified") 

    return type_str



# Joint Properties
df_joint = pd.read_csv(rf"{current_dir}\..\ExampleFiles\joints.csv") #read joints csv file
joint1 = model.getAllJointProperties()[0] # get joint 1 properties

#Assigning joint1 properties individually
joint1_type = reformat_type(df_joint.iat[0,1]) # extract and reformat joint 1 slip criterion to 'JOINT_MOHR_COULOMB' with the function 
joint1.setSlipCriterion(JointTypes[joint1_type]) # set slip criterion = mohr coulomb


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
    bolt_type = read_bolt_props.iloc[1] # get the bolt type name
    bolt_type_str = reformat_type(bolt_type) # reformat type name to 'TIEBACK_BOLT' with reformat function  
    bolt_props.setBoltType(BoltTypes[bolt_type_str]) # set bolt type = Tieback

    # read and set bolt properties for each bolt
    bolt_props.Tieback.setBondShearStiffness(float(df_bolt.iat[index,2])) # set'Bond Shear Stiffness'
    bolt_props.Tieback.setBondStrength(float(df_bolt.iat[index, 3])) # set 'Bond Strength'
    bolt_props.Tieback.setBoreholeDiameter(float(df_bolt.iat[index, 4])) # set'Borehole Diameter'
    bolt_props.Tieback.setPreTensioningForce(float(df_bolt.iat[index, 5])) # set 'Pre-Tensioning Force'
    bolt_props.Tieback.setPercentageBondLength(int(df_bolt.iat[index, 6])) # set 'Percentage Bond Length'


# Save and close file
model.saveAs(r"C:\Users\Public\Documents\Rocscience\RS2 Examples\Scripting\ExampleFiles\Anchored Sheet Pile Wall (Final)_import.fez")
model.close

# maximum displacement value on the wall








