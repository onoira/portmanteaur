#!/usr/bin/env python3

import os
from typing import Any
from setuptools import find_packages, setup

PACKAGE = 'portmanteaur'

REQUIRED = [
    'bs4',
    'html5lib',
    'requests',
]
EXTRAS: dict[str, list[str]] = {}

here = os.path.abspath(os.path.dirname(__file__))
about: dict[str, Any] = {}
with open(os.path.join(here, PACKAGE.lower(), '__version__.py')) as fp:
    exec(fp.read(), about)

try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as fp:
        long_description = '\n' + fp.read()
except FileNotFoundError:
    long_description = about['__description__']

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    python_requires=about['PYTHON_REQUIRES'],
    url=about['__url__'],
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    entry_points={
        'console_scripts': ['portmanteaur=portmanteaur.__main__:main']
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license=about['__license__']
)
