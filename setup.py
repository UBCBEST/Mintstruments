from setuptools import setup, find_packages

setup(
   name='Mintstrument',
   version='0.1',
   author='Axel Jacobsen',
   author_email='axelnj44@gmail.com',
   package_dir={'': 'src'},
   packages=find_packages('src'),
   license='LICENSE.txt',
   description='Mock packages for UBC BEST instrumentation',
   long_description=open('README.md').read(),
)

