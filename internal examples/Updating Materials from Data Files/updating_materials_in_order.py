from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

import os

'''
This script seeks to demonstrate a common pattern using RS2Modeler class 
to read csv data using the standard csv or pandas library and set on the model in the order read. 
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
mat_data_file_name = "ordered_mat_data.csv"
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

    # Set data by row index
    mats = model.getAllMaterialProperties()
    for index, row in enumerate(reader): # or use itertools zip function 
        # Get material in order
        mat = mats[index]
        # set properties from data
        mat.setMaterialName(row[0])
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

output_path = rf'{output_dir}\import {mat_data_file_name_no_path_no_ext} using standard reader set in order.fez'
model.saveAs(output_path)


# Using Pandas csv reader #######################################################
# Pandas is a powerful library for data manipulation and analysis
import pandas as pd

# Open model
model = modeler.openFile(rf"{current_dir}\{model_name}")

# Read Material Property Data skipping header rows
df_mat = pd.read_csv(mat_data_file_path, skiprows=3)

# Set data by row index
mats = model.getAllMaterialProperties() # get a list of all materials in model
for row in df_mat.itertuples():
    # Get material in order
    mat = mats[row[0]] # or row.index
    # set properties from data
    mat.InitialConditions.setUnitWeight(float(row[2])) # or row.unit_weight
    mat.Stiffness.Isotropic.setPoissonsRatio(float(row[3])) # or row.poissons_ratio
    mat.Stiffness.Isotropic.setYoungsModulus(float(row[4])) # or row.youngs_modulus
    # assume a Mohr-Coulomb material 
    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Strength.MohrCoulombStrength.setPeakCohesion(float(row[5])) # or row.cohesion
    mat.Strength.MohrCoulombStrength.setResidualCohesion(float(row[5])) # or row.cohesion
    mat.Strength.MohrCoulombStrength.setPeakFrictionAngle(float(row[6])) # or row.friction_angle
    mat.Strength.MohrCoulombStrength.setResidualFrictionAngle(float(row[6])) # or row.friction_angle

output_path = rf'{output_dir}\import {mat_data_file_name_no_path_no_ext} using pandas set in order.fez'
model.saveAs(output_path)





