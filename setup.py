#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="oauth2",
      version="1.2.1",
      description="Library for OAuth version 1.0a.",
      author="Joe Stump",
      author_email="joe@simplegeo.com",
      maintainer="Zac Bowling",
      maintainer_email="zac@zacbowling.com",
      url="http://github.com/simplegeo/python-oauth2",
      packages = find_packages(),
      install_requires = ['httplib2'],
      license = "MIT License",
      keywords="oauth",
      zip_safe = True,
      tests_require=['nose', 'coverage', 'mox'],
      classifiers=[
          'Intended Audience :: Developers',
          'Development Status :: 5 - Stable',
          'Programming Language :: Python',
      ]
)
