# This file contains function linkcode_resolve, based on
# https://github.com/numpy/numpy/blob/main/doc/source/conf.py,
# which is licensed under the BSD 3-Clause "New" or "Revised"
# license: ./licenses/numpy.rst

import configparser
import os
import sys
import subprocess
import inspect

from importlib.metadata import Distribution
from packaging.requirements import Requirement

# TODO: the first works in CI but not in my build, not sure why
# sdk_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sdk_directory = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, sdk_directory)

os.system('dwave install --yes inspector')   # To run doctests on examples with inspector

# -- Project information - these are special values used by sphinx. -------

from dwaveoceansdk import __version__ as version
from dwaveoceansdk import __version__ as release

setup_cfg = configparser.ConfigParser()
setup_cfg.read(os.path.join(sdk_directory, 'setup.cfg'))

copyright = 'D-Wave Quantum Inc' #setup_cfg['metadata']['author']

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
numfig = True

source_suffix = ['.rst', '.md']

root_doc = 'index'

language = 'en'

add_module_names = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*/shared/*.rst',]

linkcheck_ignore = [r'.clang-format',                    # would need symlink
                    r'setup.cfg',                        # would need symlink (for dimod)
                    r'https://cloud.dwavesys.com/leap',  # redirects, many checks
                    r'https://scipy.org',                # ignores robots
                    r'https://epubs.siam.org',           # ignores robots since Feb 2023
                    r'LICENSE',                          # would need symlink, checked by submodule
                    r'CONTRIBUTING',                     # would need symlink, checked by submodule
                    r'^https?://cloud\.dwavesys\.com/leap(\/.*)?$', # redirects, many checks
                    r'^https?://(.*\.)?cloud\.dwavesys\.com/sapi(\/.*)?$', # not pingable
                    r'^https://www\.sciencedirect\.com\/science\/article\/pii(\/.*)?$', # site rejects robots since March 2023
                    r'^https://onlinelibrary\.wiley\.com(\/.*)?$', # site rejects robots since March 2023
                    r'^http://science\.sciencemag\.org\/content(\/.*)?$', # site rejects robots since March 2023 
                    r'^https://iopscience\.iop\.org\/article(\/.*)?$', # site rejects robots since November 2023 
                    r'^https://journals\.aps\.org(\/.*)?$', # site rejects robots since October 2024
                    r'^https://doi\.org(\/.*)?PhysRev(.*)?$', # redirects to journals.aps.org above
                    r'^https://ssrn\.com(\/.*)?$', # site rejects robots since October 2024
                    r'^https?://dx\.doi\.org(\/.*)?ssrn\.(.*)?$', # redirects to SSRN above
                    r'^https://support\.dwavesys\.com', # Leap support site rejects robots
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
breathe_projects = {
    "minorminer": os.path.join(sdk_directory, 'minorminer/docs/build-cpp/xml/'),
    "dimod": os.path.join(sdk_directory, 'dimod/docs/build-cpp/xml/'),
    "dwave-preprocessing": os.path.join(sdk_directory, 'dwave-preprocessing/docs/build-cpp/xml/'),
    }

breathe_default_members = ('members', )
breathe_default_project = "minorminer"




# TESTING WITHOUT BUILD WARNINGS
if os.environ.get('READTHEDOCS', False):
    os.environ["DOXYGEN_QUIET"] = "YES"
    os.environ["DOXYGEN_WARNINGS"] = "NO"
    os.environ["DOXYGEN_WARN_LOGFILE"] = "/dev/null"
    #subprocess.call('cd ../minorminer/docs/; make cpp > /dev/null 2>&1', shell=True)
    subprocess.call('cd ../dimod/docs/; make cpp > /dev/null 2>&1', shell=True)
    subprocess.call('cd ../dwave-preprocessing/docs/; make cpp > /dev/null 2>&1', shell=True)
    subprocess.call('cd ../dwave-gate/; python dwave/gate/simulator/operation_generation.py', shell=True)






# TODO restore this:

# we want to build the c++ docs in RTD with all warnings:
# if os.environ.get('READTHEDOCS', False):
#     subprocess.call('cd ../minorminer/docs/; make cpp', shell=True)
#     subprocess.call('cd ../dimod/docs/; make cpp', shell=True)
#     subprocess.call('cd ../dwave-preprocessing/docs/; make cpp', shell=True)
#     subprocess.call('cd ../dwave-gate/; python dwave/gate/simulator/operation_generation.py', shell=True)

# we want to build the c++ docs in CircleCI without warnings
# and without minorminer because it generates ~500 warnings
if os.environ.get('CI', False):
    os.environ["DOXYGEN_QUIET"] = "YES"
    os.environ["DOXYGEN_WARNINGS"] = "NO"
    os.environ["DOXYGEN_WARN_LOGFILE"] = "/dev/null"
    #subprocess.call('cd ../minorminer/docs/; make cpp > /dev/null 2>&1', shell=True)
    subprocess.call('cd ../dimod/docs/; make cpp > /dev/null 2>&1', shell=True)
    subprocess.call('cd ../dwave-preprocessing/docs/; make cpp > /dev/null 2>&1', shell=True)
    subprocess.call('cd ../dwave-gate/; python dwave/gate/simulator/operation_generation.py', shell=True)

autodoc_type_aliases = {
    'numpy.typing.ArrayLike': 'numpy.typing.ArrayLike',
}

# -- Options for HTML output ----------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Ocean.svg"

# Temporary for current pydata_sphinx_theme==0.8. Will update per
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html#add-favicons
# when https://github.com/dwavesystems/dwave-ocean-sdk/pull/274 is merged
html_favicon = 'https://www.dwavesys.com/favicon.ico'

html_theme_options = {
    "github_url": "https://github.com/dwavesystems/dwave-ocean-sdk",
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
    "icon_links": [
        {
            "name": "Leap",
            "url": "https://cloud.dwavesys.com/leap/",
            "icon": "_static/Dots.svg",
            "type": "local",
        },
    ],
    "collapse_navigation": True,
    "header_links_before_dropdown": 5,
    "navbar_align": "left",
    "show_prev_next": False,
    "logo": {
        "image_light": "_static/DWave.svg",
        "image_dark": "_static/DWaveWhite.svg",
    },
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
    'urllib3': ('https://urllib3.readthedocs.io/en/stable/', None),
    'requests': ('https://requests.readthedocs.io/en/stable/', None),
    }


# -- Linkcode -------------------------------------------------------------
github_map = {'dwavebinarycsp': 'dwavebinarycsp',
              'cloud': 'dwave-cloud-client',
              'dimod':  'dimod',
              'gate': 'dwave-gate',
              'dwave_networkx': 'dwave_networkx',
              'greedy': 'dwave-greedy',
              'hybrid': 'dwave-hybrid',
              'inspector': 'dwave-inspector',
              'minorminer': 'minorminer',
              'neal': 'dwave-neal',
              'optimization': 'dwave-optimization',
              'penaltymodel': 'penaltymodel',
              'preprocessing': 'dwave-preprocessing',
              'samplers': 'dwave-samplers',
              'system': 'dwave-system',
              'embedding': 'dwave-system',
              'tabu': 'dwave-tabu'}

reqs = map(Requirement, Distribution.from_name('dwave-ocean-sdk').requires)
pkgs = [Distribution.from_name(req.name) for req in reqs]
versions = {pkg.name: pkg.version for pkg in pkgs}

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

# global substitutions
rst_epilog = """
.. |copy| unicode:: U+000A9 .. COPYRIGHT SIGN
.. |deg| unicode:: U+00B0
.. |nbsp| unicode:: 0xA0    .. non-breaking space
.. |nb-| unicode:: U+2011  .. Non-breaking hyphen (e.g., "D |nb-| Wave")
    :trim:
.. |reg| unicode:: U+000AE .. REGISTERED SIGN
.. |tm| unicode::  U+2122
.. |Darr| unicode:: U+02193 .. DOWNWARDS ARROW from docutils/parsers/rst/include/isonum.txt
.. |Uarr| unicode:: U+02191 .. UPWARDS ARROW from docutils/parsers/rst/include/isonum.txt

.. |array-like| replace:: array-like    .. used in dwave-optimization
.. _array-like: https://numpy.org/devdocs/glossary.html#term-array_like

.. |adv2| unicode:: Advantage2
.. |adv2_tm| unicode:: Advantage2 U+2122
.. |cloud| unicode:: Leap
.. _cloud: https://cloud.dwavesys.com/leap
.. |cloud_tm| unicode:: Leap U+2122
.. _cloud_tm: https://cloud.dwavesys.com/leap
.. |dwave_2kq| unicode:: D-Wave U+00A0 2000Q
.. |dwave_5kq| unicode:: Advantage
.. |dwave_5kq_tm| unicode:: Advantage U+2122
.. |dwave_short| unicode:: D-Wave
.. _dwave_short: https://dwavequantum.com
.. |dwave_short_tm| unicode:: D-Wave U+2122 U+0020
.. |dwave_system| unicode:: D-Wave U+00A0 System

.. |dwave_launch_tm| unicode:: D U+2011 Wave U+00A0 Launch U+2122
.. _dwave_launch_tm: https://www.dwavesys.com/solutions-and-products/professional-services
.. |dwave_launch| unicode:: D U+2011 Wave U+00A0 Launch
.. _dwave_launch: https://www.dwavesys.com/solutions-and-products/professional-services
.. |dwave_learn_tm| unicode:: D U+2011 Wave U+00A0 Learn U+2122
.. _dwave_learn_tm: https://training.dwavequantum.com
.. |dwave_learn| unicode:: D U+2011 Wave U+00A0 Learn
.. _dwave_learn: https://training.dwavequantum.com

.. |support_email| replace:: D-Wave Customer Support
.. _support_email: support@dwavesys.com

.. |doc_operations| replace:: *D-Wave Quantum Computer Operations*

.. |max_qubits| replace:: 5640
.. |max_couplers| replace:: 40484
.. |max_j_junctions| replace:: 1,000,000
"""

# TODO: check which of these is used

latex_preamble = r"""
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{braket}
\usepackage{siunitx}

\newcommand{\argmin}{\operatornamewithlimits{argmin}}
\newcommand{\argmax}{\operatornamewithlimits{argmax}}
\newcommand{\vc}[1]{{\pmb{#1}}}
\newcommand{\ip}[2]{\langle{#1},{#2}\rangle}
\newcommand{\sign}{\operatorname{sign}}
\newcommand {\pauli}[2]{\hat\sigma_{#1}^{(#2)}}
\newcommand{\tr}{\operatorname{tr}}
"""
