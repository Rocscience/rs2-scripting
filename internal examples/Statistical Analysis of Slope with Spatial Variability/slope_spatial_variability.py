import os

from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *

import matplotlib.pyplot as plt
import numpy as np

from DiscreteFunctionHelpers import DiscreteFunctionHelpers as DFHelpers
from FileUtilities import FileUtilities as FileUtil

'''
This script demonstrates how to conduct a statistical analysis of a slope
considering spatial variability of the soil strength.

100 samples are created with varying strength properties and slope stability analysis using 
shear strength reduction method are conducted for each model.

The Critical SRF (Factor of Safety) data is extracted from computed models to generate a
histogram of Critical SRF along with statistical results:
mean, standard deviation, min/max, probability of failure and reliability index

Custom FileUtilities and DiscreteFunctionHelpers class are created to show how 
a user could extend the functionality of the RS2 Python API library for their specific needs:
- FileUtilies class provides support for finding and managing files.
- DiscreteFunctionHelpers imports the RS2 module DiscreteFunction to provide custom support for 
    creating discrete function materials in RS2 from read data. The data could come from Slide2, 
    MATLAB scripts, Python scripts, and so on

'''

# Current folder location
current_dir = os.path.dirname(os.path.abspath(__file__)) 

# Manage the processes to run
# You can also write a function for each process which is handy for reusing in trying other cases
create_models = True
compute_models = False
extract_data = True
analyze_results = True

# Create models
if create_models:
    # Start RS2 Modeler
    RS2Modeler.startApplication(port=60054)
    modeler = RS2Modeler(port=60054)
    
    # Base file
    base_file_name = 'slope example.fez'
    base_file_path = rf'{current_dir}\{base_file_name}'

    # Output folder
    #output_dir = rf'{current_dir}\samples 5'
    output_dir = rf'{current_dir}\samples'
    os.makedirs(output_dir, exist_ok=True) 

    # Discrete function files
    #discrete_function_file_extensions = 'fn6' # make this a tuple to find more
    discrete_function_file_extensions = 'txt' 
    data_dir = rf'{current_dir}\data'
    discrete_function_file_paths = FileUtil.findFilesWithExtension(data_dir, discrete_function_file_extensions)

    # Generate sample models and compute       
    DFHelpers.importDiscreteFunctionFilesToRS2(modeler, base_file_path, discrete_function_file_paths, output_dir, compute_models)

# Extract results
srf_data = []
if extract_data:
    # Result folder
    output_dir = rf'{current_dir}\sample results 5'
    #output_dir = rf'{current_dir}\sample results'
    # Open RS2 interpreter
    RS2Interpreter.startApplication(port=60055)
    interpreter = RS2Interpreter(port=60055)

    # Get all sample models
    sample_model_file_paths = FileUtil.findFilesWithExtension(output_dir,'fez')

    # Extract data
    sample_nums = []
    for sample_model_file_path in sample_model_file_paths:
        model_results = interpreter.openFile(sample_model_file_path)
        sample_num, _ = os.path.splitext(os.path.basename(sample_model_file_path))
        sample_nums.append(int(sample_num))
        srf_data.append(model_results.getCriticalSRF())
        model_results.close()
    
    print(srf_data)
else:
    # Extracted data for 100 samples
    srf_data = [1.02, 1.02, 1.02, 1.07, 1.01, 0.99, 0.97, 1.12, 1.05, 1.11, 1.01, 1.07, 1.07, 1.08, 1.03, 1.01, 1.02, 1.09, 1.07, 1.05, 1.01, 1.09, 1.0, 1.08, 1.04, 1.04, 1.01, 1.06, 1.0, 1.05, 1.09, 0.98, 1.07, 1.14, 1.04, 1.05, 1.07, 1.04, 1.08, 1.06, 1.12, 1.03, 1.03, 1.09, 1.05, 0.95, 1.18, 0.98, 1.01, 1.05, 1.01, 1.02, 1.07, 1.03, 1.04, 1.1, 1.04, 1.15, 1.08, 1.13, 1.12, 1.03, 1.13, 1.01, 1.13, 1.02, 1.07, 1.07, 1.11, 0.99, 1.06, 1.07, 1.08, 1.1, 1.05, 1.09, 1.13, 1.09, 1.11, 1.0, 1.0, 0.98, 1.1, 1.08, 1.04, 1.08, 1.05, 0.95, 1.06, 1.07, 1.07, 1.07, 1.05, 1.05, 1.0, 1.01, 1.0, 1.09, 1.01, 0.95]

# Analyze results
if analyze_results:
    # SRF where values below are considered failure
    srf_failure_threshold = 1
    
    # Get typical statistical values
    srf_mean = np.mean(srf_data)
    srf_std = np.std(srf_data)
    srf_min = np.min(srf_data)
    srf_max = np.max(srf_data)

    # Get srf values below threshold of failure
    srf_failed = [srf for srf in srf_data if srf < srf_failure_threshold]
    # Get probability of failure
    srf_prob_of_failure = len(srf_failed)/len(srf_data) * 100
    # Get reliability index
    # assuming a normal distribution of SRF of values    
    srf_reliability_index_norm = (srf_mean-srf_failure_threshold)/srf_std 
    # assuming a lognormal distribution of SRF values
    coeff_of_variation = srf_std/srf_mean
    srf_reliability_index_log = np.log(srf_mean/np.sqrt(1+coeff_of_variation*coeff_of_variation))/np.sqrt(np.log(1+coeff_of_variation*coeff_of_variation)) 

    # Create histogram

    # Create the histogram for all data
    srf_counts, bins = np.histogram(srf_data, bins=30, density=True)
    plt.hist(bins[:-1], bins, weights=srf_counts, color='blue', edgecolor='black', alpha=0.7, label=f'Other Data')

    # Create the histogram for the highlighted region
    highlighted_data = [srf for srf in srf_data if srf < srf_failure_threshold]
    if len(highlighted_data) > 0:
        highlighted_counts = []
        highlighted_bins = []    
        for i in range(len(bins)-1):
            if bins[i] < srf_failure_threshold:
                highlighted_counts.append(srf_counts[i])
                highlighted_bins.append(bins[i])
            else:
                break

        highlighted_bins.append(bins[i])
        plt.hist(highlighted_bins[:-1], highlighted_bins, weights=highlighted_counts, color='orange', edgecolor='black', alpha=0.7, label=f'Highlighted')

    # Add labels and legend
    plt.xlabel('Factor of Safety (Critical SRF)')
    plt.ylabel('Relative Frequency')
    plt.title(f"Highlighted Data = Factor of Safety < {srf_failure_threshold} ({len(highlighted_data)} points)")
    plt.legend(loc='upper right', bbox_transform=plt.gca().transAxes)

    # Adjust the layout to make room for more items
    #plt.subplots_adjust(bottom=0.5)

    # Add textboxes with information about the plot
    info_text = (
        f'mean = {srf_mean:.3f}\n'
        f's.d. = {srf_std:.3f}\n'
        f'min = {srf_min:.3f}\n'
        f'max = {srf_max:.3f}\n'
        f'PF = {srf_prob_of_failure:.3f}%\n'
        f'RI(norm) = {srf_reliability_index_norm:.3f}\n'
        f'RI(log) = {srf_reliability_index_log:.3f}\n'
    )

    # Place the textbox on the plot
    plt.text(0.05, 0.95, info_text, fontsize=12, 
            horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes)

    # Show the plot
    plt.show()
            


    




