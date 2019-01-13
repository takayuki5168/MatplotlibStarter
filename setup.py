#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

__version__ = '0.0.1'

setup(
    name='matplotlib-starter',
    version=__version__,
    packages=find_packages(),
    description="Starter of Matplotlib",
    long_description=open('README.md').read(),
    author='Takayuki Murooka',
    author_email='takayuki5168@gmail.com',
    url='https://github.com/takayuki5168/MatplotlibStarter',
    install_requires=open('requirements.txt').readlines(),
    #package_data={'matplotlib_starter': listup_package_data()},
    license='MIT',
    keywords='utility'
)
