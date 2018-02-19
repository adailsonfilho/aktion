# packaged following: https://packaging.python.org/

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="aktion",
      version="0.1.0", description="An pipeline framework based ",
      author="Adailson de Castro Queiroz Filho",
      author_email="adailsonfilho@gmail.com",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 3.6'],
      keywords='pipeline json process',
      packages=find_packages(exclude=['examples']))
