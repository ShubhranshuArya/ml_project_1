# Helps in building the ML Project as a package which can later be used in other packages.

from setuptools import find_packages, setup
from typing import List

def install_requirements(file_path:str) -> List[str]:
    '''
    Returns the list of requirements.
    '''
    hyphen_e_dot = '-e .'
    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines
        requirements = [x.replace("\n", "") for x in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Shubhranshu',
    author_email='shubhranshuarya@gmail.com',
    packages=find_packages(),
    install_requires=install_requirements('requirements.txt')
)