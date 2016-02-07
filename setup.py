#!/usr/bin/env python
# encoding: utf-8

# n.b. we can't have unicode_literals here due to http://bugs.python.org/setuptools/issue152
from __future__ import absolute_import, division, print_function

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

install_requires = [
    'Django',
]

setup(
    name='haystack-geoshapes',
    version='0.0.1',
    description='Add support for elastic search geoshapes.',
    author='Ben Scott',
    author_email='ben@benscott.co.uk',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'geoshapes'
    ],
    zip_safe=False,
    install_requires=install_requires,
)
