# Setup.py is used to install src as a local package in the system or virtual environment
from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'Vedant Jain',
    author_email= 'vedantj890@gmail.com',
    packages= find_packages(), # find_packages() will look for constructor file in each and every folder & in whatever folder the file is found that folder will be considered as local package
    install_requires = []

)