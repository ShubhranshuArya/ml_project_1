# Helps in building the ML Project as a package which can later be used in other packages.

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    Returns the list of requirements.
    '''
    hyphen_e_dot = '-e .'
    requirements = []

    with open(file_path) as file_obj:
        # Call readlines() to read the lines of the file
        requirements = file_obj.readlines()
        # Strip newline characters from each line
        requirements = [x.strip() for x in requirements if x.strip() != hyphen_e_dot]
        print(requirements)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Shubhranshu',
    author_email='shubhranshuarya@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)