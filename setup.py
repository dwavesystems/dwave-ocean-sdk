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

install_requires = [
    'dwave-networkx>=0.6.1,<0.7.0',
    'dwave-system>=0.5.0,<0.6.0',
    'dwave-qbsolv>=0.2.7,<0.3.0',
    'dwave-neal>=0.4.0,<0.5.0'
]

extras_require = {
    ':(platform_machine == "x86_64" or platform_machine == "amd64") and python_version != "3.4"': [
        'dwavebinarycsp[mip]>=0.0.7,<0.1.0'
    ],
    ':platform_machine != "x86_64" and platform_machine != "amd64" or python_version == "3.4"': [
        'dwavebinarycsp[maxgap]>=0.0.7,<0.1.0'
    ]
}

packages = ['dwaveoceansdk']

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

python_requires = '>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*'

setup(
    name='dwave-ocean-sdk',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave-ocean-sdk',
    long_description=open('README.rst').read(),
    classifiers=classifiers,
    python_requires=python_requires,
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require
)
