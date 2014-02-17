import os
import sys

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    license = "License :: OSI Approved :: Apache Software License",
    zip_safe = False,

    author = 'HGVS Contributors',
    author_email = 'reecehart+hgvs@gmail.com',
    description = """HGVS Integration Test""",
    long_description = "ensure that 'pip install hgvs' works",
    name = "hgvs-integration-test",
    packages = find_packages(),
    url = 'https://bitbucket.org/invitae/hgvs-integration-test',

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python",
        "Topic :: Database :: Front-Ends",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        ],
    keywords = [
        'bioinformatics',
        'computational biology',
        'genome variants',
        'genome variation',
        'genomic variants',
        'genomic variation',
        'genomics',
        'hgvs',
        ],

    install_requires = [
        'hgvs',
        ],
    )

## <LICENSE>
## Copyright 2014 HGVS Contributors (https://bitbucket.org/invitae/uta)
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## </LICENSE>
