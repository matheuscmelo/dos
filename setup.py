from setuptools import setup, find_packages

setup(
    name='dos',
    version='1.0',
    author='Matheus Melo',
    install_requires=[
        "requests==2.21.0"
    ],
    packages=find_packages()
)
