import os
from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name = "ADPY",
    version = "0.12 alpha",
    author = "Oliver Schnabel",
    author_email = "zwenson@rocketmail.com",
    description = ("ADPY is a Python library for algorithmic differentiation"),
    license = "GPLv3",
    keywords = "python algorithmic differentiation scientific numpy",
    url = "https://github.com/zwenson/ADPY",
    packages=['ADPY','ADPY.ADFUN','ADPY.SOLVER'],
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
)