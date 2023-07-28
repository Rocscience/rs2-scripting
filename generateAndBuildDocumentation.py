import subprocess

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
    run_sphinx_build()
