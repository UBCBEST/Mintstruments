from setuptools import setup

setup(
   name='Mintstrument',
   version='0.0.0',
   author='Axel Jacobsen',
   author_email='axelnj44@gmail.com',
   packages=['mintstrument', 'minstrument.mock_smbus2', 'tests'],
   scripts=[],
   license='LICENSE.txt',
   description='Mock packages for UBC BEST instrumentation',
   long_description=open('README.md').read(),
   install_requires=[],
)

