# -*- coding: utf-8 -*-
#   Copyright 2014 Sameer Suhas Marathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Setup file for EulerLib"""

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='eulerlib',
      version='0.0.1',
      description=('A library of number theory related '
                   'functions inspired by Project Euler.'),
      long_description=readme(),
      url='',
      author='Sameer Marathe',
      author_email='transmogrifier@gmail.com',
      license='Apache License 2.0',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop'
      ],
      keywords='mathematics project_euler number_theory prime_numbers',
      packages=['eulerlib'],
      install_requires=[
      'bitarray'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)

