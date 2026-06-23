import papermill as pm
import os

folderNames = ["support", "support_functions"]
# folderNames = ["hydraulic", "material", "model", "results", "support", "support_functions"]

for forlderName in folderNames:    
    folder = os.path.join(os.path.abspath(""), "docs", "example_code", forlderName)

    notebooks = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb")
    ]

    # Save the current working directory
    orig_cwd = os.getcwd()

    try:
        # Change to docs folder before running notebooks
        os.chdir(os.path.join(os.path.abspath(""), "docs", "example_code", "example_models"))

        for nb in notebooks:
            print(f"Running notebook: {nb}")
            pm.execute_notebook(
                input_path=nb,
                output_path=nb,  # overwrite executed notebook
                cwd=os.path.abspath("")
            )
    finally:
        # Restore original working directory
        os.chdir(orig_cwd)
