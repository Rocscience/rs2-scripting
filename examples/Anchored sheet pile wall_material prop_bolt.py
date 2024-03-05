from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os
import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np

# Start RS2 Modeler and Interpreter
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open model
current_dir = os.path.dirname(os.path.abspath(__file__))
model = modeler.openFile(rf"{current_dir}\..\ExampleFiles\Anchored Sheet Pile Wall (Final)_default.fez")

# Import the Excel file
excel_data = pd.ExcelFile (rf"{current_dir}\..\ExampleFiles\data.xlsx") #open Excel file

# Function 1: convert string to enum value
def string_to_enum(EnumTypes: Enum, value: str):
    try:
        return EnumTypes[value]
    except KeyError:
        raise ValueError(f"Invalid value '{value}' for provide EnumTypes")

# Function 2:  remove units from column names in a DataFrame
def remove_units(df, column_name):   
    def remove_units_col(col_name):
        # Split the column name by '(' and take the first part, only when '(' or ' ' is found
        if '(' in col_name or ' ' in col_name:
            return col_name.split('(')[0].strip()
        else:
            return col_name
    # Rename the columns using the function
    df.rename(columns={column_name:remove_units_col(column_name)}, inplace=True)

# Function 3
# write a function to define fuzzy data, and return 
# 1) bolt type name, and 2) bolt type input name

# Define a function to reformat bolt type names based on similarity
def reformat_type(bolt_type):
    type_lower = bolt_type.lower()

    if 'end' in type_lower or 'anchored' in type_lower:
        type_str = 'END_ANCHORED' # use to set type, need to be Enum
        #type_input = EndAnchored # use to set type properties
    elif 'fully' in type_lower or 'bonded' in type_lower:
        type_str = 'FULLY_BONDED'
        #type_input = FullyBonded
    elif 'plain' in type_lower or 'strand' in type_lower or 'queens' in type_lower or 'cable' in type_lower:
        type_str = 'QUEENS_CABLE'
        #type_input = PlainStrandCable
    elif 'swellex' in type_lower or 'split' in type_lower or 'set' in type_lower or 'shear' in type_lower:
        type_str = 'SHEAR_BOLT'
        #type_input = Swellex
    elif 'tieback' in type_lower:
        type_str = 'TIEBACK_BOLT'
        #type_input = Tieback
    else:
        raise ValueError(f"Type name '{bolt_type}' cannot be identified") 

    return type_str
    #return type_str, type_input 


# Joint Properties

df_joint = excel_data.parse('Joint') #read joint tab data
print(excel_data.parse('Joint'))

joint_type = df_joint.at[0,'Slip Criterion'] # extract joint 1 slip criterion

joint_props = model.getJointPropertyByName((df_joint.at[0,'Name']))
joint_props.setSlipCriterion(string_to_enum(JointTypes, joint_type))


# Bolt Properties (Excel Import)

df_bolt = excel_data.parse('Bolt') #read bolt tab data

# get/set bolt properties for each bolt
for index, read_bolt_props in df_bolt.iterrows():
    print("Index:",index) 

    # remove units from column names
    for column_label, _ in read_bolt_props.items():
        print("Old column name:" ,column_label) #test result
        remove_units(df_bolt, column_label) # rename column name in DataFrame with Function 2
    print("New column name:" ,df_bolt.columns) #test result

    bolt_props = model.getBoltPropertyByName(read_bolt_props['Name']) # get the bolt properties by name

    # reformat Type data
    read_bolt_type = read_bolt_props['Type'] # get the type
    type_str = reformat_type(read_bolt_type) # reformat type name with reformat function  
    type_enum = string_to_enum(BoltTypes, type_str) # string to enum with the enum function
    bolt_props.setBoltType(type_enum) # set bolt type 

    # read and set bolt properties by bolt type
    if type_enum == BoltTypes.TIEBACK_BOLT:
        print(df_bolt.at[index, 'Bond Shear Stiffness'])
        bolt_props.Tieback.setBondShearStiffness(df_bolt.at[index, 'Bond Shear Stiffness'])
        bolt_props.Tieback.setBondStrength(df_bolt.at[index, 'Bond Strength'])
        bolt_props.Tieback.setBoreholeDiameter(df_bolt.at[index, 'Borehole Diameter'])
        bolt_props.Tieback.setPreTensioningForce(df_bolt.at[index, 'Pre-Tensioning Force'])
        bolt_props.Tieback.setPercentageBondLength(df_bolt.at[index, 'Percentage Bond Length'])
    else: 
        # Add elif if there are other bolt types you want to handle
        pass #WHAT?


'''
    # using Tieback as an input
    # read and set bolt properties by bolt type
    bolt_props.type_input.BondShearStiffness = read_bolt_props['Bond Shear Stiffness']
    bolt_props.type_input.BondStrength = read_bolt_props['Bond Strength']
    bolt_props.type_input.BoreholeDiameter = read_bolt_props['Borehole Diameter']
    bolt_props.type_input.PreTensioningForce = read_bolt_props['Pre-Tensioning Force']
    bolt_props.type_input.PercentageBondLength = read_bolt_props['Percentage Bond Length']
    '''



# Liner Properties

    # Read liner properties from Excel File

df_liner = excel_data.parse('Liner') #read liner tab data
print(excel_data.parse('Liner'))

liner1_name = df_liner.at[0,'Name'] #read liner 1 name
print(liner1_name, type(liner1_name))

liner1_thickness = df_liner.at[0,'Thickness (m)'] #read liner 1 thickness
print(liner1_thickness, type(liner1_thickness))

    # Read liner properites from RS2
linerList = model.getAllLinerProperties() #get all liner properties
liner1 = linerList[0]

liner1.setLinerName(liner1_name) # set liner 1 name
liner1.StandardBeam.setThickness(liner1_thickness) #set liner 1 thickness


# Save and close file
model.saveAs(r"C:\Users\Public\Documents\Rocscience\RS2 Examples\Scripting\ExampleFiles\Anchored Sheet Pile Wall (Final)_import.fez")
model.close


