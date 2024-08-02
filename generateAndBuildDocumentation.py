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

def remove_undoc_members_from_specific_files():
    rstFilesFolder = "docs/generatedAPIDocFiles"
    files_to_modify = ['rs2.interpreter.InterpreterEnums.rst',
                       'rs2.interpreter.InterpreterGraphEnums.rst',
                       'rs2.interpreter.supportResults.BoltResult.rst',]

    for filename in files_to_modify:
        filepath = os.path.join(rstFilesFolder, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                lines = file.readlines()

            # Remove :undoc-members: if present
            with open(filepath, "w") as file:
                for line in lines:
                    if ":undoc-members:" not in line:
                        file.write(line) 

def reorder_rst_files():
    rstFilesFolder = "docs/generatedAPIDocFiles"
    files_to_modify = ['rs2.interpreter.rst',
                       'rs2.modeler.properties.bolt.rst',
                       'rs2.modeler.properties.joint.rst',
                       'rs2.modeler.properties.material.hydraulic.rst',
                       'rs2.modeler.properties.material.stiffness.rst',
                       'rs2.modeler.properties.material.strength.rst',
                       'rs2.modeler.properties.material.strength.rst',
                       'rs2.modeler.properties.pile.rst',
                       'rs2.modeler.properties.rst',
                       'rs2.modeler.rst',
                       'rs2.rst',]

    for filename in files_to_modify:
        filepath = os.path.join(rstFilesFolder, filename)
        
        with open(filepath, 'r') as file:
            lines = file.readlines()

        automodule_section = []
        toctree_section = []
        other_sections = []

        current_section = other_sections
        automodule_directive = ".. automodule:: "
        toctree_directive = ".. toctree::"

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith(automodule_directive):
                current_section = automodule_section
            elif stripped_line.startswith(toctree_directive):
                current_section = toctree_section
            current_section.append(line)

        # Concatenate the sections in the desired order
        new_content = other_sections + automodule_section + ["\n"] + toctree_section

        with open(filepath, 'w') as file:
            file.writelines(new_content)

def add_line_to_file(file_path, line):
    try:
        # Open the file in append mode
        with open(file_path, 'a') as file:
            # Write the new line to the file
            file.write(line + '\n')
        print(f"Line added to '{file_path}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
    except IOError as e:
        print(f"An error occurred while writing to '{file_path}': {e}")

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
    remove_undoc_members_from_specific_files()
    reorder_rst_files()
    add_line_to_file("docs/generatedAPIDocFiles/rs2.utilities.ApplicationManager.rst", "   :exclude-members: minimumPort, maximumPort, defaultTimeout")
    add_line_to_file("docs/generatedAPIDocFiles/rs2.utilities.ColorPicker.rst", "   :exclude-members: Black, Brown, Dark_Olive_Green, Dark_Green, Dark_Teal, Dark_Blue, Indigo, Dark_Grey, Dark_Red, Orange, Dark_Yellow, Green, Teal, Blue, Blue_Grey, Grey_40, Red, Light_Orange, Lime, Sea_Green, Aqua, Light_Blue, Violet, Grey_50, Pink, Gold, Yellow, Bright_Green, Turquoise, Skyblue, Plum, Light_Grey, Rose, Tan, Light_Yellow, Pale_Green, Pale_Turquoise, Pale_Blue, Lavender, White")
    run_sphinx_build()
