from __future__ import absolute_import

import sys
from setuptools import setup

_PY2 = sys.version_info.major == 2

# add __version__, __author__, __authoremail__, __description__ to this namespace
# equivalent to:
if _PY2:
    execfile("./dwaveoceansdk/package_info.py")
else:
    exec(open("./dwaveoceansdk/package_info.py").read())

install_requires = ['dwavebinarycsp>=0.0.2,<0.1.0',
                    'dwave-networkx>=0.6.1,<0.7.0',
                    'dwave-system>=0.3.0,<0.4.0',
                    'dwave-qbsolv>=0.2.7,<0.3.0',
                    'dwave-neal>=0.3.0,<0.4.0'
                    ]

packages = ['dwaveoceansdk']

setup(
    name='dwave-ocean-sdk',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave-ocean-sdk',
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires
)
