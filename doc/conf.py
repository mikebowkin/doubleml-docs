# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'DoubleML'
copyright = '2021, Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M.'
author = 'Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M.'

# The full version, including alpha/beta/rc tags
# release = '0.2.dev0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'matplotlib.sphinxext.plot_directive',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'sphinx_copybutton',
    'sphinx_panels',
    'jupyter_sphinx',
]

# sphinx-panels shouldn't add bootstrap css since the pydata-sphinx-theme
# already loads it
panels_add_bootstrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'shared/*']

master_doc = 'index'

autoclass_content = 'class'
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'github_url': 'https://github.com/DoubleML/doubleml-for-py',
    'navigation_with_keys': False,
}

# html_logo = '../img/logo.png'
html_extra_path = ['../img/logo.png']
html_favicon = '../img/favicon.ico'

html_sidebars = {'**': ['logo.html',
                        'search-field.html',
                        'sidebar-nav-bs.html']}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: | {2,5}\.\.\.\.:'
copybutton_prompt_is_regexp = True

# config of sphinx gallery for examples
nbsphinx_prolog = r"""
.. raw:: html
    {% raw %}
        <div class="admonition note">
        <p class="admonition-title">Note</p>
        <ul class="simple">
    {% endraw %}
    Download Jupyter notebook:
    {{ '<' }}a class={{ '"' }}reference external{{ '"' }} href={{ '"' }}https://docs.doubleml.org/stable/{{ env.doc2path(env.docname, base=None) }}{{ '"' }}{{ '>' }}https://docs.doubleml.org/stable/{{ env.doc2path(env.docname, base=None) }}{{ '</a>' }}.
    {% raw %}
        </ul>
        </div>
    {% endraw %}
"""

# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'statsmodels': ('https://www.statsmodels.org/stable/', None),
}

# To execute R code via jupyter-execute one needs to install the R kernel for jupyter
# https://github.com/IRkernel/IRkernel

jupyter_execute_default_kernel = 'ir'
jupyter_sphinx_linenos = True
