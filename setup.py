# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
Converts SVG images to PDF in case the builder does not support
SVG images natively (e.g. LaTeX).
'''

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-svg2pdfconverter',
    version='0.1.0',
    url='https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter',
    download_url='https://pypi.org/project/sphinxcontrib-svg2pdfconverter',
    license='BSD',
    author='Stefan Wiehler',
    author_email='stefan.wiehler@missinglinkelectronics.com',
    description='Sphinx SVG to PDF converter extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
