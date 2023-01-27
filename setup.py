
from setuptools import setup, find_packages

setup(
    name='cl_test_package',
    version='0.1',
    description='A sample Python package',
    author='Cormac Lynch',
    author_email='cormac.lynch1@ucdconnect.ie',
    packages=find_packages(),
    install_requires=[
        'socket',
        'os','platform','psutil'
    ],
)
