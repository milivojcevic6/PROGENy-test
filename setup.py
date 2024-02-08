from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A Python package for analyzing data using the PROGENy algorithm.'
LONG_DESCRIPTION = 'PROGENyTest is a Python package designed to facilitate data analysis using the PROGENy algorithm. With this package, users can efficiently analyze their datasets, leveraging the power of PROGENy to uncover biological insights and interpret gene expression data. PROGENyTest provides a user-friendly interface and comprehensive functionality, making it easy for researchers to integrate PROGENy into their data analysis pipelines.'

# Setting up
setup(
    name="PROGENyTest",
    version=VERSION,
    author="Milivojcevic6",
    author_email="milivojcevic@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url = "https://github.com/milivojcevic6/PROGENy-test",
    # install_requires=['test1','test2'],
    keywords=['python', 'PROGENy', 'analysis', 'cancer', 'gene expression', 'data analysis', 'genialis'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
    ]
)