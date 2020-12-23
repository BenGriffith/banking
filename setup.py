# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Banking Project',
    long_description=readme,
    author='Ben Griffith',
    author_email='bengriffith@outlook.com',
    url='https://github.com/bengriffith/banking',
    license=license,
    packages=find_packages(exclude=('tests', 'doc'))
)

