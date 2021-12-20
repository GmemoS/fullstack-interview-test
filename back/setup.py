from setuptools import find_packages, setup

setup(
    name='git_manager',
    version='1.0',
    description='Lib for manage git repository.',
    author='Carlos Guillermo Jimenez Salcedo',
    package_dir={'': 'libs'},
    packages=find_packages(where='libs'),
    install_requires=[],
)
