from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Clean newlines and extra spaces
        requirements = [req.replace("\n", "").strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='AutoValuate',
    version='0.0.1',
    author='Shant Kumar P Gokavi',
    author_email='gokavishantkumar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)