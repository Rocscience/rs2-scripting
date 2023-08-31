import subprocess
import re

"""
sphinx-apidoc Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
sphinx-build Documentation: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
"""

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
        "src/rs2/Client.py",
        "src/rs2/proxyObjects/documentProxy.py",
        "src/rs2/proxyObjects/propertyProxy.py",
        "src/rs2/ProxyObject.py"
    ]
    subprocess.run(cmd, check=True)

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
    run_sphinx_build()
