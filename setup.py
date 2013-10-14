#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name             = 'cssmin',
    version          = '0.2.0',
    author           = "Zachary Voase",
    author_email     = "zacharyvoase@me.com",
    url              = 'http://github.com/zacharyvoase/cssmin',
    description      = "A Python port of the YUI CSS compression algorithm.",
    py_modules       = ['cssmin'],
    package_dir      = {'': 'src'},
    entry_points     = {'console_scripts': ['cssmin = cssmin:main']},
)
