# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Specify the directory path
directory_path = os.path.abspath('..')
directory_path2 = os.path.abspath('../rs2')
directory_path3 = os.path.abspath('../rs2/proxyObjects')


# Add the directory path to sys.path
sys.path.insert(0, directory_path)
sys.path.insert(0, directory_path2)
sys.path.insert(0, directory_path3)

print(sys.path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RS2 Scripting Client Library'
copyright = '2023, Rocscience Inc.'
author = 'Rocscience Inc.'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']
# autodoc_mock_imports = ['rs2']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'rs2.Client']

# -- Options for LaTeX output -------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble' : '',
    'figure_align' : 'htbp'
}

latex_logo = '_static/logo.png'