import subprocess
import os
import shutil
"""
sphinx-apidoc Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
sphinx-build Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
"""

#see https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-b
html = 'html'
singleHtml = 'singlehtml'

builder = singleHtml

def set_sphinx_apidoc_settings():
    # Command to set SPHINX_APIDOC_OPTIONS environment variable
    export_cmd = "export SPHINX_APIDOC_OPTIONS=members"
    
    # Use shell=True to execute the command with the shell
    subprocess.run(export_cmd, shell=True, check=True)

def run_sphinx_apidoc():
    # Command to run sphinx-apidoc
    # sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN …]
    # --force: Force overwriting of any existing generated files.
    # .py files listed are ignored from documentation generation

    cmd = [
        "sphinx-apidoc",
        "--force",
        "--module-first",
        "-o",
        "docs/generatedAPIDocFiles",
        "src/rs2",
        "src/rs2/_common/Client.py",
        "src/rs2/_common/documentProxy.py",
        "src/rs2/modeler/properties/propertyProxy.py",
        "src/rs2/_common/ProxyObject.py"
    ]
    subprocess.run(cmd, check=True)

def remove_subpackage_submodule_headers():
    rstFilesFolder = "docs/generatedAPIDocFiles"
    linesToRemove = ["Submodules\n", "----------\n", "Subpackages\n", "-----------\n"]
    for listedFile in os.listdir(rstFilesFolder):
        filepath = os.path.join(rstFilesFolder, listedFile)
        with open(filepath, "r") as file:
            lines = file.readlines()
        with open(filepath, "w") as file:
            for line in lines:
                if line not in linesToRemove:
                    file.write(line)
    

def run_sphinx_build():
    # Command to run sphinx-build
    # sphinx-build [options] <sourcedir> <outputdir> [filenames …]

    cmd = [
        "sphinx-build", 
        "-b", 
        builder, 
        "docs", 
        f"docs/_build/{builder}"
        ]
    subprocess.run(cmd, check=True)

def clear_generated_docs():
    # Specify the path of the folder you want to delete
    folder_path = 'docs/generatedAPIDocFiles'

    # Check if the folder exists before attempting to delete it
    if os.path.exists(folder_path):
        # Use shutil.rmtree() to delete the folder and its contents recursively
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents deleted successfully.")
    else:
        print(f"Folder '{folder_path}' does not exist.")
if __name__ == "__main__":
    clear_generated_docs()
    run_sphinx_apidoc()
    remove_subpackage_submodule_headers()
    run_sphinx_build()
