from setuptools import find_packages,setup

from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this funstion will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace('\n',"") for req in requirements]
    return requirements


setup(
name = 'ml-projects',
version = '0.0.1',
author = 'navraj',
package = find_packages(),
install_packages = get_requirements('requirements.txt')

)