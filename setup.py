from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='basic sorting and recursion functions in python',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/xolisa003/palgorithms',
    author='Xolisa Mzini',
    author_email='xolisa.mzini@gmail.com'
)
