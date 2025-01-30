#for installation nd packages

from setuptools import find_packages ,setup # to check packages

#from typing import List
def get_requirements()->list(str):
    requirements_list=list[str]==[]
    return requirements_list

setup(

name='Sensor-Fault-Detection',
version="0.0.1",
author='mayur',
author_email='mayurajankar151998@gmail.com',
packages=find_packages(),
install_requires=get_requirements(),
     
)