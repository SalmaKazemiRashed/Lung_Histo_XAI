# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # so autodoc can find your code

# -- Project information -----------------------------------------------------
project = 'Histology_XAI'
copyright = '2025, AitsLab'
author = 'Salma Kazemi Rashed'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',       # pull in docstrings from your code
    'sphinx.ext.napoleon',      # support for Google/Numpy style docstrings
    'sphinx.ext.viewcode',      # link to highlighted source code
    'sphinx.ext.githubpages',   # create .nojekyll for GitHub Pages
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'  # or 'alabaster', 'sphinx_rtd_theme', etc.
html_static_path = ['_static']
