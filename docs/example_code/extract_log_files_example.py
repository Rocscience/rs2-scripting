import os
import zipfile

def extract_files_from_fez(filePath, file_extensions):
    """
    Extract specified file types from a .fez file.

    This function takes the path to a .fez file and a list of file extensions.
    It extracts files matching the given extensions from the .fez file without 
    extracting the entire contents. The extracted file paths are returned in a list.
    """

    all_extract_file_path = []
    with zipfile.ZipFile(filePath, 'r') as zip_ref:
        # Find all files in the zip that match the extensions
        extract_files = [f for f in zip_ref.namelist() if any(f.endswith(ext) for ext in file_extensions)]

        # If files are found, return the file path
        if extract_files:
            for file in extract_files:
                # extract the file with specified extension without unzipping the RS2 file
                zip_ref.extract(file, current_dir)
                
                # get the extracted file path               
                extract_file_path = os.path.join(current_dir, file)
                all_extract_file_path.append(extract_file_path)
    
        return all_extract_file_path
                
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = rf"{current_dir}\example_models\ExampleModel.fez"

# Log files' file extensions
log_extensions = {".log", ".low", ".lot"}

# Call the function to extract log files
file_paths = extract_files_from_fez(file_path, log_extensions)
print("Extracted File Path(s):")
print(*file_paths, sep = '\n')
