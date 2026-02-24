# -*- coding: utf-8 -*-
"""
    sphinxcontrib.rsvgconverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Converts SVG images to PDF or PNG using libRSVG in case the builder does not
    support SVG images natively (e.g. LaTeX).

    :copyright: Copyright 2018-2023 by Stefan Wiehler
                <sphinx_contribute@missinglinkelectronics.com>.
    :license: BSD, see LICENSE.txt for details.
"""
from .rsvgconverter import RSVGConverter


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_post_transform(RSVGConverter)
    app.add_config_value('rsvg_converter_bin', 'rsvg-convert', 'env')
    # Applies to both PDF and PNG output
    app.add_config_value('rsvg_converter_args', [], 'env')
    # Only applies to PDF output
    app.add_config_value('rsvg_converter_format', 'pdf', 'env')

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
