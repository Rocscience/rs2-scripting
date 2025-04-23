import os
import zipfile

def check_convergence(filePath):
    """
    To detect convergence after stress analysis, stage number and convergence flag 
    are extracted from the .rng file inside the .fez file.

    If the model didn't converge, the unstable stage number will be returned.
    If all stages converge, the model will return None.
    """

    with zipfile.ZipFile(filePath, 'r') as model_file:
        # Find the .rng file
        rng_file = next((f for f in model_file.namelist() if f.endswith('.rng')), None)
        
        if not rng_file:
            raise FileNotFoundError("No .rng file found in the given file.")

        with model_file.open(rng_file) as file:
            stage, converged_flag = None, None
            for line in file:
                decoded_line = line.decode('utf-8').strip()
                if decoded_line.startswith("* Stage number ="):
                    value  = decoded_line.split('=')[1].strip()
                    if value.isdigit():
                        stage = int(value)
                
                # If the model doesn't converge at this stage, stage converged flag 
                # will be raised
                elif decoded_line.startswith("* Stage converged flag ="):
                    value = decoded_line.split('=')[1].strip()
                    if value.isdigit():
                        converged_flag = int(value)
                        if converged_flag == 1:
                            return stage

    return None

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = rf"{current_dir}\example_models\UserWarningModel.fez"

stage = check_convergence(file_path)
if stage != None:
    print(f"At stage {stage}, model didn't converge.")
else:
    print("Model converged.")