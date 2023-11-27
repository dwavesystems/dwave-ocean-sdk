# -*- coding: utf-8 -*-

# This file contains function linkcode_resolve, based on
# https://github.com/numpy/numpy/blob/main/doc/source/conf.py,
# which is licensed under the BSD 3-Clause "New" or "Revised"
# license: ./licenses/numpy.rst

import configparser
import os
import sys
import subprocess
import inspect
import pkg_resources

sdk_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, sdk_directory)

os.system('dwave install --yes inspector')   # To run doctests on examples with inspector

# -- Project information - these are special values used by sphinx. -------

from dwaveoceansdk import __version__ as version
from dwaveoceansdk import __version__ as release

setup_cfg = configparser.ConfigParser()
setup_cfg.read(os.path.join(sdk_directory, 'setup.cfg'))

author = setup_cfg['metadata']['author']
copyright = setup_cfg['metadata']['author']

project = 'Ocean Documentation'

# Also add our own 'special value', the minimum supported Python version
rst_prolog = f"""
.. |python_requires| replace:: {setup_cfg['options']['python_requires']}
"""

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.linkcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'breathe',
    'sphinx_design',
    'reno.sphinxext',
    'sphinx_copybutton',
]

autosummary_generate = True

source_suffix = ['.rst', '.md']

root_doc = 'index'  # before Sphinx 4.0, named master_doc

add_module_names = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

linkcheck_ignore = [r'.clang-format',                    # would need symlink
                    r'setup.cfg',                        # would need symlink (for dimod)
                    r'https://cloud.dwavesys.com/leap',  # redirects, many checks
                    r'https://scipy.org',                # ignores robots
                    r'https://epubs.siam.org',           # ignores robots since Feb 2023
                    r'LICENSE',                          # would need symlink, checked by submodule
                    r'CONTRIBUTING',                     # would need symlink, checked by submodule
                    ]

pygments_style = 'sphinx'

todo_include_todos = True

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

doctest_global_setup = """
import operator         # Used by dwave-binarycsp

# Set up mocking for DWaveSampler
from dwave.system.testing import MockDWaveSampler
import dwave.system
import hybrid
dwave.system.DWaveSampler = MockDWaveSampler
hybrid.samplers.DWaveSampler = MockDWaveSampler

from dwave.system import *
from dwave.embedding import *

import networkx as nx
import dwave_networkx as dnx

import dimod
import dwavebinarycsp

from hybrid.samplers import *
from hybrid.core import *
from hybrid.utils import *
from hybrid.decomposers import *
from hybrid.composers import *
from hybrid.flow import *

import penaltymodel

import dwave.inspector
"""

# -- Breathe configuration ------------------------------------------------

# Path to the cpp xml files
breathe_projects = {"minorminer": os.path.join(
                      sdk_directory, 'minorminer/docs/build-cpp/xml/'),
                    "dimod": os.path.join(
                      sdk_directory, 'dimod/docs/build-cpp/xml/'),
                    "dwave-preprocessing": os.path.join(
                      sdk_directory, 'dwave-preprocessing/docs/build-cpp/xml/'),
                    }

breathe_default_members = ('members', )
breathe_default_project = "minorminer"

# we want to build the c++ docs in RTD
if os.environ.get('READTHEDOCS', False):
    subprocess.call('cd ../minorminer/docs/; make cpp', shell=True)
    subprocess.call('cd ../dimod/docs/; make cpp', shell=True)
    subprocess.call('cd ../dwave-preprocessing/docs/; make cpp', shell=True)

# -- Options for HTML output ----------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Ocean.svg"

html_theme_options = {
    "github_url": "https://github.com/dwavesystems/dwave-ocean-sdk",
    "external_links": [
        {
            "url": "https://docs.dwavesys.com/docs/latest/index.html",
            "name": "System Docs",
        },
        {
            "url": "https://docs.dwavesys.com/docs/latest/legal.html",
            "name": "Legal",
        },
    ],
    "icon_links": [
        {
            "name": "Leap",
            "url": "https://cloud.dwavesys.com/leap/",
            "icon": "_static/Dots.svg",
            "type": "local",
        },
    ],
    "collapse_navigation": True,
    "header_links_before_dropdown": 8,
    "navbar_align": "left",  
    "show_prev_next": False,
    "logo": {
        "image_light": "_static/Ocean.svg",
        "image_dark": "_static/Ocean.svg",
    }
}
html_sidebars = {
    "**": ["sidebar-nav-bs"]  # remove ads
}
html_static_path = ['_static']

def setup(app):
   app.add_css_file('theme_overrides.css')
   app.add_css_file('cookie_notice.css')
   app.add_js_file('cookie_notice.js')
   app.add_config_value('target', 'sdk', 'env')

# -- Intersphinx ----------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('http://numpy.org/doc/stable/', None),
    'networkx': ('https://networkx.org/documentation/stable/', None),
    'sysdocs_gettingstarted': ('https://docs.dwavesys.com/docs/latest/', None),
    'oceandocs': ('https://docs.ocean.dwavesys.com/en/stable/', None),
    }


# -- Linkcode -------------------------------------------------------------
github_map = {'dwavebinarycsp': 'dwavebinarycsp',
              'cloud': 'dwave-cloud-client',
              'dimod':  'dimod',
              'gate': 'dwave-gate',
              'dwave_networkx': 'dwave-networkx',
              'greedy': 'dwave-greedy',
              'hybrid': 'dwave-hybrid',
              'inspector': 'dwave-inspector',
              'minorminer': 'minorminer',
              'neal': 'dwave-neal',
              'penaltymodel': 'penaltymodel',
              'preprocessing': 'dwave-preprocessing',
              'samplers': 'dwave-samplers',
              'system': 'dwave-system',
              'embedding': 'dwave-system',
              'tabu': 'dwave-tabu'}

reqs = pkg_resources.get_distribution('dwave-ocean-sdk').requires(extras=['all'])
pkgs = [pkg_resources.get_distribution(req) for req in reqs]
versions = {pkg.project_name: pkg.version for pkg in pkgs}

def linkcode_resolve(domain, info):
    """
    Find the URL of the GitHub source for dwave-ocean-sdk objects.
    """
    # Based on https://github.com/numpy/numpy/blob/main/doc/source/conf.py
    # Updated to work on multiple submodules and fall back to next-level
    # module for objects such as properties

    if domain != 'py':
        return None

    obj={}
    obj_inx = 0
    obj[obj_inx] = sys.modules.get(info['module'])
    for part in info['fullname'].split('.'):
        obj_inx += 1
        try:
            obj[obj_inx] = getattr(obj[obj_inx - 1], part)
        except Exception:
            pass

    # strip decorators, which would resolve to the source of the decorator
    # https://bugs.python.org/issue34305
    for i in range(len(obj)):
           obj[i] = inspect.unwrap(obj[i])

    fn = None
    for i in range(len(obj)-1, -1, -1):
        try:
           fn = inspect.getsourcefile(obj[i])
           if fn:
              obj_inx = i
              break
        except:
           pass

    linespec = ""
    try:
        source, lineno = inspect.getsourcelines(obj[obj_inx])
        if obj_inx != 0:
           linespec = "#L%d" % (lineno)
    except Exception:
        linespec = ""

    if not fn or not "site-packages" in fn:
       return None

    if ".egg" in fn:
       fn = fn.replace(fn[:fn.index("egg")+len("egg")], "")
    else:
       fn = fn.replace(fn[:fn.index("site-packages")+len("site-packages")], "")

    repo = fn.split("/")[1] if  \
           (fn.split("/")[1] != "dwave") \
           else fn.split("/")[2]

    pm_module = github_map[repo]
    pm_ver = versions[github_map[repo]]
    fn = "https://github.com/dwavesystems/{}/blob/{}{}".format(pm_module, pm_ver, fn)

    return fn + linespec
