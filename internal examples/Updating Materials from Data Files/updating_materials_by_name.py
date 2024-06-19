from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

import os

'''
This script seeks to demonstrate a common pattern using RS2Modeler class 
to read csv data using the standard csv or pandas library and set on the model by name. 
'''

# Start RS2 Modeler
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Current directory 
current_dir = os.path.dirname(os.path.abspath(__file__))

# Output directory
output_dir = rf"{current_dir}\results"
os.makedirs(output_dir, exist_ok=True)

# Model to change
model_name = 'Twin Tunnel.fez'

# Material data
mat_data_file_name = "unordered_mat_data.csv"
mat_data_file_name_no_path_no_ext = os.path.splitext(os.path.basename(mat_data_file_name))[0]
mat_data_file_path = rf"{current_dir}\{mat_data_file_name}"

# Using Python standard csv reader ##########################################################
import csv

# Open model
model = modeler.openFile(rf"{current_dir}\{model_name}")

# Read csv file
with open(mat_data_file_path,'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Skip header lines
    next(reader,None)
    next(reader,None)
    next(reader,None)
    next(reader,None)

    # Set data using material name
    for index, row in enumerate(reader): # or use itertools zip function 
        # Get material by name
        mat_name = row[0]
        mat = model.getMaterialPropertyByName(mat_name)
        # set properties from data
        mat.InitialConditions.setUnitWeight(float(row[1]))
        mat.Stiffness.Isotropic.setPoissonsRatio(float(row[2]))
        mat.Stiffness.Isotropic.setYoungsModulus(float(row[3]))
        # assume a Mohr-Coulomb material 
        mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
        mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
        mat.Strength.MohrCoulombStrength.setPeakCohesion(float(row[4]))
        mat.Strength.MohrCoulombStrength.setResidualCohesion(float(row[4]))
        mat.Strength.MohrCoulombStrength.setPeakFrictionAngle(float(row[5]))
        mat.Strength.MohrCoulombStrength.setResidualFrictionAngle(float(row[5]))

output_path = rf'{output_dir}\import {mat_data_file_name_no_path_no_ext} using standard reader set by name.fez'
model.saveAs(output_path)


# Using Pandas csv reader #######################################################
# Pandas is a powerful library for data manipulation and analysis
# NOTE: Also check out their support to read other data formats:
#       xlsx, json, html, xml, sql, and many more
import pandas as pd

# Open model
model = modeler.openFile(rf"{current_dir}\{model_name}")

# Read Material Property Data skipping header rows
df_mat = pd.read_csv(mat_data_file_path, skiprows=3)

# Set data by material name
for row in df_mat.itertuples():
    # Get material by name
    mat_name = row.name # or row['name'] or row[1]
    mat = model.getMaterialPropertyByName(mat_name)
    # set properties from data
    mat.InitialConditions.setUnitWeight(float(row.unit_weight)) # or row['unit_weight'] or row[2]
    mat.Stiffness.Isotropic.setPoissonsRatio(float(row.poissons_ratio)) # or row['poissons_ratio'] or row[3]
    mat.Stiffness.Isotropic.setYoungsModulus(float(row.youngs_modulus)) # or row['youngs_modulus'] or row[4]
    # assume a Mohr-Coulomb material 
    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Strength.MohrCoulombStrength.setPeakCohesion(float(row.cohesion)) # or row['cohesion'] or row[5]
    mat.Strength.MohrCoulombStrength.setResidualCohesion(float(row.cohesion)) # or row['cohesion'] or row[5]
    mat.Strength.MohrCoulombStrength.setPeakFrictionAngle(float(row.friction_angle)) # or row['friction_angle'] or row[6]
    mat.Strength.MohrCoulombStrength.setResidualFrictionAngle(float(row.friction_angle)) # or row['friction_angle'] or row[6]

output_path = rf'{output_dir}\import {mat_data_file_name_no_path_no_ext} using pandas set by name.fez'
model.saveAs(output_path)





