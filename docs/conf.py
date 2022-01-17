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
rst_prolog = f" .. |python_requires| replace:: {setup_cfg['options']['python_requires']}"

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
    'sphinx_panels'
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
                    r'LICENSE',                          # would need symlink, checked by submodule
                    r'CONTRIBUTING',                     # would need symlink, checked by submodule
                    ]

pygments_style = 'sphinx'

todo_include_todos = True

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

import penaltymodel.core as pm
import penaltymodel.cache as pmc
#import penaltymodel.maxgap as maxgap
import penaltymodel.mip as mip
import penaltymodel.lp as lp

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

# we want to build the c++ docs in RTD
if os.environ.get('READTHEDOCS', False):
    subprocess.call('cd ../minorminer/docs/; make cpp', shell=True)
    subprocess.call('cd ../dimod/docs/; make cpp', shell=True)
    subprocess.call('cd ../dwave-preprocessing/docs/; make cpp', shell=True)

# -- Options for HTML output ----------------------------------------------

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']


def setup(app):
   app.add_css_file('theme_overrides.css')
   app.add_css_file('cookie_notice.css')
   app.add_js_file('cookie_notice.js')
   app.add_config_value('target', 'sdk', 'env')


# -- Intersphinx ----------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'bson': ('https://api.mongodb.com/python/current/', None),
    'networkx': ('https://networkx.org/documentation/stable/', None),
    'sysdocs_gettingstarted': ('https://docs.dwavesys.com/docs/latest/', None),
    'oceandocs': ('https://docs.ocean.dwavesys.com/en/stable/', None),
    }


# -- Linkcode -------------------------------------------------------------
github_map = {'dwavebinarycsp': 'dwavebinarycsp',
              'cloud': 'dwave-cloud-client',
              'dimod':  'dimod',
              'dwave_networkx': 'dwave-networkx',
              'greedy': 'dwave-greedy',
              'hybrid': 'dwave-hybrid',
              'inspector': 'dwave-inspector',
              'minorminer': 'minorminer',
              'neal': 'dwave-neal',
              'penaltymodel': {'cache': 'penaltymodel_cache',
                               'core': 'penaltymodel_core',
                               'lp': 'penaltymodel_lp',
                               'maxgap': 'penaltymodel_maxgap',
                               'mip': 'penaltymodel_mip'},
              'preprocessing': 'dwave-preprocessing',
              'system': 'dwave-system',
              'embedding': 'dwave-system',
              'tabu': 'dwave-tabu'}

reqs = pkg_resources.get_distribution('dwave-ocean-sdk').requires(extras=['all'])
pkgs = [pkg_resources.get_distribution(req) for req in reqs]
versions = {pkg.project_name: pkg.version for pkg in pkgs}
versions['penaltymodel-core'] = versions.pop('penaltymodel')

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
           (fn.split("/")[1] != "dwave") and (fn.split("/")[1] != "penaltymodel") \
           else fn.split("/")[2]

    if fn.split("/")[1] == 'penaltymodel':
        pm_module = github_map['penaltymodel'][repo] 
        pm_ver = versions[github_map['penaltymodel'][repo].replace('_', '-')]
        fn = "https://github.com/dwavesystems/penaltymodel/tree/{}-{}/{}{}".format( \
             repo, pm_ver, pm_module, fn)
    else:
        pm_module = github_map[repo] 
        pm_ver = versions[github_map[repo]]
        fn = "https://github.com/dwavesystems/{}/blob/{}{}".format(pm_module, pm_ver, fn) 
 
    return fn + linespec
