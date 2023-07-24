import subprocess

def run_sphinx_apidoc():
    # Command to run sphinx-apidoc
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

def run_sphinx_build():
    # Command to run sphinx-build
    cmd = ["sphinx-build", "-b", "html", "docs", "docs/_build/html"]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    run_sphinx_apidoc()
    run_sphinx_build()
