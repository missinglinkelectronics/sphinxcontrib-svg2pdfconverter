# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requires = ['Sphinx>=1.6.3']

setup(
    name='sphinxcontrib-svg2pdfconverter',
    version='1.2.1',
    url='https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter',
    download_url='https://pypi.org/project/sphinxcontrib-svg2pdfconverter',
    license='BSD',
    author='Stefan Wiehler',
    author_email='stefan.wiehler@missinglinkelectronics.com',
    description='Sphinx SVG to PDF converter extension',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        "CairoSVG": ['cairosvg>=1.0'],
    },
    python_requires='~=3.4',
    namespace_packages=['sphinxcontrib'],
)
