import os

from DiscreteFunctionHelpers import DiscreteFunctionHelpers as DFHelpers
from FileUtilities import FileUtilities as FileUtil

"""
This example script shows how to read discrete function data and then check
the output by writing to a file using the DiscreteFunctionHelpers class
"""

# Current folder location
current_dir = os.path.dirname(os.path.abspath(__file__)) 

# Output folder
output_dir = rf'{current_dir}\read data'
os.makedirs(output_dir, exist_ok=True) 

# Get all discrete function files (.fn6) from folder
fn6_files = FileUtil.findFilesWithExtension(os.path.join(current_dir,'data'),'fn6')

# Read and write data
for fn6_file in fn6_files:
    all_df = DFHelpers.readDiscreteFunctionFile(fn6_file)
    base_name = os.path.basename(fn6_file)
    for df in all_df:
        DFHelpers.writeDiscreteFunctionFilefn6(os.path.join(output_dir,f'read {base_name}'),df)

# Get all custom files (.cust) from folder
cust_files = FileUtil.findFilesWithExtension(os.path.join(current_dir,'data'),'cust')

# Read and write data
for cust_file in cust_files:
    all_df = DFHelpers.readDiscreteFunctionFile(cust_file)
    base_name = os.path.basename(cust_file)
    DFHelpers.writeDiscreteFunctionFileCustom(os.path.join(output_dir,f'read {base_name}'),all_df)