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

# Import the Excel file
excel_data = pd.ExcelFile (rf"{current_dir}\..\ExampleFiles\data.xlsx") #open Excel file


'''
# Joint Properties

joint_df = excel_data.parse('Joint') #read joint tab data
print(excel_data.parse('Joint'))

joint_type = joint_df.iat[0,1] #extract joint 1 slip criterion
#print(joint_df.iat[0,1])
print(joint_df.at[0, 'Slip Criterion'])


# Excel Import
# Function to convert string to enum value
def string_to_enum(EnumTypes: Enum, value: str):
    try:
        return EnumTypes[value]
    except KeyError:
        raise ValueError(f"Invalid value '{value}' for provide EnumTypes")

for joint in jointList:
    joint.setSlipCriterion(string_to_enum(read_string))
'''


# Bolt Properties
bolt_tab = excel_data.sheet_names[2] #Bolt tab


# Define a function to remove units from column names
def remove_units(column_name):
    # Split the column name by '(' and take the first part
    return column_name.split('(')[0].strip()

# Rename the columns using the remove_units function
df.rename(columns=remove_units, inplace=True)

# Now the columns will have units removed from their names
print(df.head())  # Display the first few rows of the DataFrame




# bolt example

df_all_bolt_props = pd.ExcelFile ('Bolt') # read bolt tab

# get/set bolt properties for each bolt
for index, read_bolt_props in df_all_bolt_props.iterrows():
    print("Index:",index) 

    # remove units from column names
    for column_name in read_bolt_props.items():
        remove_units(column_name)
        print("New column name:" ,column_name)

    

    bolt_props = getBoltPropertyByName(read_bolt_props['Name'])
    read_bolt_type = read_bolt_props['Type'] # get the type
    read_bolt_type_enum = string_to_enum(BoltTypes, read_bolt_type)
    bolt_props.setBoltType(read_bolt_type_enum)
    if read_bolt_type_enum == BoltTypes.TIEBACK_BOLT:
        bolt_props.Tieback.BondShearStiffness = read_bolt_props["Bond Shear Stiffness"]
    else: 
        # Add elif if there are other bolt types you want to handle
        pass #WHAT?






















# Liner Properties

    # Read liner properties from Excel File
liner_tab = excel_data.sheet_names[1] #Liner tab

liner_df = excel_data.parse(liner_tab) #read liner tab data
print(excel_data.parse(liner_tab))

liner1_name = liner_df.at[0,'Name'] #read liner 1 name
print(liner1_name, type(liner1_name))

liner1_thickness = liner_df.at[0,'Thickness (m)'] #read liner 1 thickness
print(liner1_thickness, type(liner1_thickness))

    # Read liner properites from RS2
linerList = model.getAllLinerProperties() #get all liner properties
liner1 = linerList[0]

liner1.setLinerName(liner1_name) # set liner 1 name
liner1.StandardBeam.setThickness(liner1_thickness) #set liner 1 thickness




