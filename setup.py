'''
The setup.py file is an essential part of packaging
and distributing python projects.It is used by setuptools 
(or distutils in old python version ) to define the configuration
of your project , such as metadata , dependency and more
'''
from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:

    '''
    This function will return list of requirements
    '''

    try:
        requirement_list:List[str]=[]
        with open('requirements.txt','r') as file:
            #Read line from the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore the empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
        return requirement_list
    
    except FileNotFoundError:
        print('requirement.txt file not found')

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="Sarvjeet kumar",
    author_email='jha.sarvjeet1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)

