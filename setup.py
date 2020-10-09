# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='fhmake',
    version='2020.2.1',
    description='Provides multiple methods to hide and retrieve data',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/FHMake/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/FHMake",
        "repository":
            "https://github.com/FHPythonUtils/FHMake"
    },
    author='FredHappyface',
    classifiers=[
        'Environment :: Console', 'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    entry_points={"console_scripts": ["fhmake = fhmake:cli"]},
    packages=['FHMake'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'pdoc3==0.*,>=0.9.1', 'simplesecurity==2020.*,>=2020.0.0',
        'tomlkit>=0.7'
    ],
    extras_require={
        "full": [
            "bandit==1.*,>=1.6.2", "dlint==0.*,>=0.10.3", "dodgy==0.*,>=0.2.1",
            "poetry==1.*,>=1.1.2", "safety==1.*,>=1.9.0"
        ]
    },
)
