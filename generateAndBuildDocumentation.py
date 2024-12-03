import subprocess
import os
import shutil
import toml

"""
sphinx-apidoc Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
sphinx-build Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
"""

#see https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-b
html = 'html'
singleHtml = 'singlehtml'

builder = html

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
        "-o",
        "docs/generatedAPIDocFiles",
        "-d", # maximum depth
        "2",
        "src/rs2", # exclude the following files
        "src/rs2/_common/Client.py",
        "src/rs2/_common/documentProxy.py",
        "src/rs2/modeler/properties/propertyProxy.py",
        "src/rs2/_common/ProxyObject.py",
        "-e" # put each module on its own page
    ]
    subprocess.run(cmd, check=True)

def update_toctree(lines):
    updated_lines = []
    in_submodule_section = False
    for line in lines:
        if line.strip() == "Submodules":
            in_submodule_section = True
        elif line.strip() == "Subpackages":
            in_submodule_section = False

        if in_submodule_section and "   :maxdepth: 2" in line:
            updated_lines.append(line.replace("   :maxdepth: 2", "   :maxdepth: 1"))
        else:
            updated_lines.append(line)

    return updated_lines

def remove_subpackage_submodule_headers():
    rstFilesFolder = "docs/generatedAPIDocFiles"
    linesToRemove = ["Submodules\n", "----------\n", "Subpackages\n", "-----------\n", "Module contents\n", "---------------\n"]
    
    for listedFile in os.listdir(rstFilesFolder):
        filepath = os.path.join(rstFilesFolder, listedFile)
        with open(filepath, "r") as file:
            lines = file.readlines()

        # Update toctree maxdepth for submodules
        lines = update_toctree(lines)

        # Remove unwanted headers
        lines = [line for line in lines if line not in linesToRemove]

        with open(filepath, "w") as file:
            file.writelines(lines)

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

def get_version_from_toml(toml_file_path):
    with open(toml_file_path, 'r') as toml_file:
        data = toml.load(toml_file)
        
    version = data.get('project', {}).get('version')
    
    if not version:
        raise ValueError("Version not found in TOML file.")
    
    return version

def update_documentation_version():
    file_path = 'pyproject.toml'
    version = get_version_from_toml(file_path)
    
    index_file_path = 'docs/index.rst'
    
    with open(index_file_path, 'r') as index_file:
        lines = index_file.readlines()
        for i, line in enumerate(lines):
            if "**Version: " in line:
                lines[i] = f"**Version: {version}**\n"

    with open(index_file_path, 'w') as index_file:
        index_file.writelines(lines)

if __name__ == "__main__":
    update_documentation_version()
    clear_generated_docs()
    run_sphinx_apidoc()
    remove_subpackage_submodule_headers()
    run_sphinx_build()
