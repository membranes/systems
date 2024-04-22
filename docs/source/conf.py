"""
Module conf.py

Notes
------

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Project information:
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

"""

import revitron_sphinx_theme


'''
Basic
'''
project = '<img src="../_static/icon.svg" alt="Systems">'
copyright = '2024, greyhypotheses'
author = 'greyhypotheses'
release = '0.1'



'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

Sphinx extension modules. Extensions are either Sphinx extensions, named 'sphinx.ext.*', 
or custom ones.  Note, myst_enable_extensions excludes 'linkify'
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    'myst_parser'
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
    'attrs_block',
    'attrs_inline'
]

'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


'''
Templates
'''
templates_path = ['_templates']
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

'''

html_theme = 'revitron_sphinx_theme'

html_static_path: list[str] = ['_static']

html_css_files: list[str] = [
    'css/generic.css',
    'css/figures.css',
    'https://fonts.googleapis.com/css?family=Vollkorn',
    'https://fonts.googleapis.com/css?family=Tangerine'
]

html_js_files: list[str] = ['https://code.jquery.com/jquery-3.7.0.min.js',
                            'https://code.highcharts.com/stock/highstock.js',
                            'https://code.highcharts.com/stock/modules/data.js',
                            'https://code.highcharts.com/stock/modules/exporting.js',
                            'https://code.highcharts.com/stock/modules/export-data.js',
                            'https://code.highcharts.com/stock/modules/accessibility.js',
                            'https://code.highcharts.com/highcharts.js',
                            'https://code.highcharts.com/modules/networkgraph.js'
                            ]

html_theme_options = {
    'color_scheme': '',
    'canonical_url': 'https://premodelling.github.io/systems/',
    'analytics_id': '',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'github_url': 'https://www.github.com/premodelling/systems',
    'logo_mobile': '_static/logo.svg'
}

html_logo = '_static/logo.svg'

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Introduction',
             'url': 'introduction/introduction.html'},
            {'title': 'Search',
             'url': 'search.html'}
        ]
    }
}

