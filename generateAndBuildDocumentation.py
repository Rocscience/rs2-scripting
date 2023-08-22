import subprocess
import re

"""
sphinx-apidoc Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
sphinx-build Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
"""

def run_sphinx_apidoc():
    # Command to run sphinx-apidoc
    # sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN …]
    # --force: Force overwriting of any existing generated files.
    # .py files listed are ignored from documentation generation

    cmd = [
        "sphinx-apidoc",
        "--force",
        "-o",
        "docs",
        "src",
        "src/rs2/Client.py",
        "src/rs2/proxyObjects/documentProxy.py",
        "src/rs2/proxyObjects/propertyProxy.py",
        "src/rs2/ProxyObject.py",
    ]
    subprocess.run(cmd, check=True)

def add_sphinx_example_modules():
    file = open("docs\modules.rst", "a")
    file.write("   examples" + '\n')

def add_example_module_links():
    exampleDict = {
        "Bolt": "- :ref:`Bolt Example`.\n",
        "Liner": "- :ref:`Liner Example`.\n",
        "Model": "- :ref:`Model Example`.\n"
    }

    file_path = 'docs/rs2.proxyObjects.rst'

    foundBasePropModule = False
    linesAfterBasePropModule = 0
    exampleFileToInsert = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        output = open(file_path, 'w')
        for line in lines:
            output.write(line)
            if " module" in line:
                for baseProp, exampleFile in exampleDict.items():
                    if baseProp in line:
                        foundBasePropModule = True
                        exampleFileToInsert = exampleFile
            if foundBasePropModule and linesAfterBasePropModule == 1:
                output.write(exampleFileToInsert)
                foundBasePropModule = False
                linesAfterBasePropModule = 0
            
            if foundBasePropModule:
                linesAfterBasePropModule += 1

def add_example_modeller_interpreter_links():
    exampleDict = {
        "Modeler": "- :ref:`Modeler Example`.\n",
        "Interpreter": "- :ref:`Interpreter Example`.\n",
    }

    file_path = 'docs/rs2.rst'

    foundBasePropModule = False
    linesAfterBasePropModule = 0
    exampleFileToInsert = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        output = open(file_path, 'w')
        for line in lines:
            output.write(line)
            if " module" in line:
                for baseProp, exampleFile in exampleDict.items():
                    if baseProp in line:
                        foundBasePropModule = True
                        exampleFileToInsert = exampleFile
            if foundBasePropModule and linesAfterBasePropModule == 1:
                output.write(exampleFileToInsert)
                foundBasePropModule = False
                linesAfterBasePropModule = 0
            
            if foundBasePropModule:
                linesAfterBasePropModule += 1


def run_sphinx_build():
    # Command to run sphinx-build
    # sphinx-build [options] <sourcedir> <outputdir> [filenames …]

    cmd = [
        "sphinx-build", 
        "-b", 
        "latex", 
        "docs", 
        "docs/_build/pdf"
        ]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    run_sphinx_apidoc()
    add_sphinx_example_modules()
    add_example_module_links()
    add_example_modeller_interpreter_links()
    run_sphinx_build()
