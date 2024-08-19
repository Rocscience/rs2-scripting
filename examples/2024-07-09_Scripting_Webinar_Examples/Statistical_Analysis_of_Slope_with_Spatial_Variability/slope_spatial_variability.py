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

Go to the "Manage the processes to run" section to enable/disable the processes you want to try.

Note that the models use a coarse mesh to reduce the computation time as to better 
showcase the functionality of this script. For a more accurate factor of safety, you will need
to refine the mesh in the model before running the script. We have provided a fine mesh model in
case you want to try this.

First, the factor of safety for the deterministic case is computed.

Depending on the selected option, 5 or 100 samples are created with varying strength properties. 
Slope stability analysis using shear strength reduction method are conducted for each model.

The Critical SRF (Factor of Safety) data is extracted from computed models to generate a
histogram of Critical SRF along with statistical results:
mean, standard deviation, min/max, probability of failure and reliability index.

Custom FileUtilities and DiscreteFunctionHelpers classes are provided to show how 
a user could extend the functionality of the RS2 Python API library for their specific needs:
- FileUtilies class provides support for finding and managing files.
- DiscreteFunctionHelpers imports the RS2 module DiscreteFunction to provide custom support for 
    creating discrete function materials in RS2 from read data. The data could come from Slide2, 
    MATLAB scripts, Python scripts, and so on

'''

# Current folder location
current_dir = os.path.dirname(os.path.abspath(__file__)) 

# Manage the processes to run ###############################################################################
# Deterministic Case
compute_deterministic_case = True              # True to compute factor of safety for base model, False otherwise

# Generating samples
use_previously_computed_sample_results = False  # True to skip generating samples and use pre-computed results, False otherwise
save_new_sample_models = True                   # True to save each generated sample model, False otherwise 
generate_five_samples_only = True               # True will generate 5 samples to see how this script works, 
                                                # False will generate all 100 samples which will take much longer to finish

# Analysis
analyze_results = True                          # True to output result plots, False otherwise


# Start analysis ###########################################################################################

# Start RS2 Modeler
RS2Modeler.startApplication(port=60054)
modeler = RS2Modeler(port=60054)

# Open RS2 interpreter
RS2Interpreter.startApplication(port=60055)
interpreter = RS2Interpreter(port=60055)

# Base file
base_file_name = 'slope example.fez' # Try 'slope example fine mesh.fez' for more accurate factor of safety, but it will take much longer to compute 
base_file_path = rf'{current_dir}\{base_file_name}'

# Deterministic Case #####################################################################################
if compute_deterministic_case:
    deterministic_dir = rf'{current_dir}\deterministic'
    os.makedirs(deterministic_dir, exist_ok=True) 
    model = modeler.openFile(base_file_path)
    model.saveAs(rf'{deterministic_dir}\slope example (deterministic).fez')
    model.compute()

# Generate samples with spatial variability of strength ##################################################
# Set use_previously_computed_sample_results = True to use previously computed results to save time
if not use_previously_computed_sample_results:

    # Output and data folders
    if generate_five_samples_only:
        samples_dir = rf'{current_dir}\samples 5'
        data_dir = rf'{current_dir}\data 5'
    else:
        samples_dir = rf'{current_dir}\samples'
        data_dir = rf'{current_dir}\data'

    os.makedirs(samples_dir, exist_ok=True)       
        
    # Discrete function file paths
    discrete_function_file_extensions = {'fn6','cust'}
    discrete_function_file_paths=[]
    for discrete_function_file_extension in discrete_function_file_extensions:
        discrete_function_file_paths.extend(FileUtil.findFilesWithExtension(data_dir, discrete_function_file_extension))

    # Collect all discrete function file data to minimize number of times models are opened in update
    samplenum_to_discretefunctiondata = DFHelpers.getDiscreteFunctionDataPerSample(discrete_function_file_paths)

    # Open base model
    model = modeler.openFile(base_file_path)

    # Save a copy that we will modify in the script, so you can easily retry this script
    base_sample_file_name = 'slope example (sampling).fez'
    base_sample_file_path = rf'{current_dir}\{base_sample_file_name}'
    model.saveAs(base_sample_file_path)

    # Key data to extract
    sample_nums = []
    srf_data = []

    # Update model(s)
    for sample_number, all_discrete_function_data in samplenum_to_discretefunctiondata.items():
        
        # Update materials
        DFHelpers.updateModelMaterialsWithDiscreteFunctionData(model,all_discrete_function_data)
        
        # Save as a new file if required
        if save_new_sample_models:
            new_sample_file_name = f'{sample_number}.fez'
            new_sample_file_path = os.path.join(samples_dir, new_sample_file_name)
            model.saveAs(new_sample_file_path)
        else:
            model.save()

        # Compute if required
        model.compute()

        # Extract results
        if save_new_sample_models:
            model_results = interpreter.openFile(new_sample_file_path)
        else:
            model_results = interpreter.openFile(base_sample_file_path)

        sample_nums.append(sample_number)
        srf_data.append(model_results.getCriticalSRF())
        model_results.close()

# Set use_previously_computed_sample_results = True to use previously computed results to save time
else:
    # Extracted data for 100 samples with a fine mesh
    sample_nums =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    srf_data =[1.022, 1.071, 1.083, 1.042, 0.952, 1.04, 1.073, 1.115, 1.074, 1.023, 1.074, 1.014, 0.988, 0.975, 1.118, 1.05, 1.108, 1.011, 1.076, 1.085, 1.032, 1.012, 1.023, 1.09, 1.068, 1.05, 1.012, 1.087, 1.007, 1.044, 1.044, 1.006, 1.059, 1.004, 1.051, 1.095, 0.978, 1.076, 1.14, 1.051, 1.069, 1.041, 1.082, 1.067, 1.124, 1.035, 1.032, 1.09, 1.05, 1.186, 0.982, 1.016, 1.049, 1.017, 1.018, 1.07, 1.033, 1.038, 1.094, 1.153, 1.089, 1.131, 1.12, 1.035, 1.137, 1.016, 1.132, 1.02, 1.069, 1.115, 0.984, 1.058, 1.067, 1.076, 1.101, 1.056, 1.091, 1.13, 1.092, 1.002, 1.001, 0.98, 1.103, 1.081, 1.045, 1.079, 1.05, 0.952, 1.065, 1.076, 1.068, 1.047, 1.048, 0.996, 1.015, 0.998, 1.09, 1.017, 0.955, 1.025]
print(sample_nums)
print(srf_data)

# Analyze sample results
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
    print('done!')
            


    




