import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ADPY",
    version = "0.11 alpha",
    author = "Oliver Schnabel",
    author_email = "zwenson@rocketmail.com",
    description = ("ADPY is a Python library for algorithmic differentiation"),
    license = "GPLv3",
    keywords = "python algorithmic differentiation scientific numpy",
    url = "https://github.com/zwenson/ADPY",
    packages=['ADPY','ADPY.ADFUN','ADPY.SOLVER'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
)