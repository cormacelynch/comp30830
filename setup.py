
from setuptools import setup, find_packages

setup(
    name='CL_first setup.py file',
    version='0.2',
    description='A sample Python package',
    author='Cormac Lynch',
    author_email='cormac.lynch1@ucdconnect.ie',
    packages=find_packages(),
    install_requires=[
        'socket',
        'os','platform','psutil'
    ],
)
