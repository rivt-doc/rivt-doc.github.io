# -- Path setup --------------------------------------------------------------
import sys
from pathlib import Path
sys.path.append(str(Path(".").resolve()))

project = 'rivt'
copyright = '2023 StructureLabs'
author = 'rholland'
release = '0.1'

myst_heading_anchors = 3

myst_enable_extensions = ['substitution', 'deflist',
                          'html_image', 'amsmath']

extensions = ['myst_parser', 'sphinx.ext.githubpages',
              "sphinxcontrib.jquery", 'sphinx_copybutton', 'sphinx_favicon']

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_context = {
    # ...
    "default_mode": "auto"
}
html_sidebars = {
    "**": ["search-field.html", "sbt-sidebar-nav.html"]}
html_theme = 'sphinx_book_theme'
html_static_path = ['_static', '_static/img/']
html_logo = "_static/img/riv-dark8c.png"
html_theme_options = {
    "show_navbar_depth": 0,
    "show_toc_level": 0,
    "home_page_in_toc": True,
    "navbar_align": "content",
    "navbar_start": ["navbar-logo"],
    "navbar_center": [],
    "navbar_end": ["navbar-icon-links"],
    "primary_sidebar_end": ["indices.html"],
    "logo": {
        "image_dark": "_static/img/riv-dark8c.png",
    }
}
favicons = [
    {"href": "favicon-32x32.png"},
    {"href": "favicon-16x16.png"},
]


# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
