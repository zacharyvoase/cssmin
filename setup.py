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
    classifiers      = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: BSD License',
    ],
    keywords         = 'css, minifier, yui, css compression',
    license          = 'BSD License',
)
