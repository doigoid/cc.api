## Copyright (c) 2010, John Doig, Creative Commons

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the "Software"),
## to deal in the Software without restriction, including without limitation
## the rights to use, copy, modify, merge, publish, distribute, sublicense,
## and/or sell copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

from setuptools import setup, find_packages
import sys

requires = [
    'setuptools',
    'mimeparse',
    'decorator',
    'lxml',
    'web.py',
    'nose',
    'cc.license',
    'WebTest',
    ]

if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name = "cc.api",
    version = "0.1",
    
    packages = ['cc.api'],
    namespace_packages = ['cc'],
    package_dir = {'':'.'},
    
    # scripts and dependencies
    install_requires = requires,

    extras_require = {
        'fcgi': ['flup'],
        },

    entry_points = {
        'console_scripts' : [
            'server = cc.api.server:serve',
            'noop = cc.api.server:noop',
            'api.fcgi = cc.api.server:fcgi',
            ],
        'paste.app_factory': [
            'api=cc.api.server:app_factory',
            ],
        },

    test_suite = 'nose.collector',
    
    # author metadata
    author = 'John E Doig III',
    author_email = 'john@creativecommons.org',
    description = 'Creative Commons REST API web service.',
    license = 'MIT',
    url = 'http://api.creativecommons.org',

    )
