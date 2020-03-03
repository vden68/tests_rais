import tests_rais

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='tests_rais',
    version=tests_rais.__version__,
    packages=find_packages(),
    url='https://github.com/vden68/tests_rais',
    license='',
    author='Vasiliy Denisov',

    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'allure-pytest',
        'requests',
    ],
)