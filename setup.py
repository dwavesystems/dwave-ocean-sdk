from __future__ import absolute_import

import sys
from setuptools import setup

_PY2 = sys.version_info.major == 2

# add __version__, __author__, __authoremail__, __description__ to this namespace
# equivalent to:
if _PY2:
    execfile("./dwave_sdk/package_info.py")
else:
    exec(open("./dwave_sdk/package_info.py").read())

install_requires = ['dimod',
                    'dwave_micro_client',
                    'dwave_networkx',
                    'dwave_micro_client_dimod']
tests_require = []
extras_require = {}

packages = ['dwave_sdk']

setup(
    name='dwave_sdk',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave_sdk',
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require
)
