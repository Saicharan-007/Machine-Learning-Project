from setuptools import setup
from typing import List
from setuptools import find_packages


#declaring the variables for setup

PROJECT_NAME='housing-predictor'
VERSION='0.0.3'
AUTHOR='Sai Charan Reddy Chiluka'
DESCRIPTION='This is a first Machine learning project'
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file 
    return this function is going to return a list which contain name of 
    libraries mentioned in requirements.txt.file
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e.")

setup(name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)



