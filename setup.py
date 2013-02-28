#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distribute_setup import use_setuptools; use_setuptools()
from setuptools import setup


__version__ = '0.1.4'

setup(
    name             = 'cssmin',
    version          = __version__,
    author           = "Zachary Voase",
    author_email     = "zacharyvoase@me.com",
    url              = 'http://github.com/zacharyvoase/cssmin',
    description      = "A Python port of the YUI CSS compression algorithm.",
    py_modules       = ['cssmin'],
    package_dir      = {'': 'src'},
    entry_points     = {'console_scripts': ['cssmin = cssmin:main']},
)
