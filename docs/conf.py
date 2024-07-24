# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Specify the directory path
directory_path = os.path.abspath(os.path.join('..', 'src'))


# Add the directory path to sys.path
sys.path.insert(0, directory_path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RS2 Scripting Reference Manual'
copyright = '2024, Rocscience Inc.'
author = 'Rocscience Inc.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx_copybutton', 
              'sphinx.ext.napoleon',
              'sphinx_rtd_theme']

autodoc_default_options = {
    'member-order': 'bysource',
}

napoleon_google_docstring = True
napoleon_use_param = True
napoleon_use_ivar = True

autosummary_generate = True

exclude_patterns = ['generatedAPIDocFiles/modules.rst']

# -- Options for LaTeX output -------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble' : '',
    'figure_align' : 'htbp'
}

html_logo = '_static/logo.png'

# html_theme = "sphinx_rtd_theme"
html_theme = 'pydata_sphinx_theme'
