# -*- coding: utf-8 -*-
"""
    sphinxcontrib.inkscapeconverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Converts SVG images to PDF or PNG using Inkscape in case the builder does not
    support SVG images natively (e.g. LaTeX).

    :copyright: Copyright 2018-2023 by Stefan Wiehler
                <sphinx_contribute@missinglinkelectronics.com>.
    :license: BSD, see LICENSE.txt for details.
"""
from .inkscapeconverter import InkscapeConverter


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_post_transform(InkscapeConverter)
    app.add_config_value('inkscape_converter_bin', 'inkscape', 'env')
    app.add_config_value('inkscape_converter_args',
            ['--export-area-drawing'], 'env')

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
