# -*- coding: utf-8 -*-
"""
    sphinxcontrib.cairosvgconverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Converts SVG images to PDF or PNG using CairoSVG in case the builder does not
    support SVG images natively (e.g. LaTeX).

    See <https://cairosvg.org/>.

    :copyright: Copyright 2018-2023 by Stefan Wiehler
                <sphinx_contribute@missinglinkelectronics.com> and
                Copyright 2020 by Marko Kohtala
                <marko.kohtala@gmail.com>.
    :license: BSD, see LICENSE.txt for details.
"""
from .cairosvgconverter import CairoSVGConverter


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_post_transform(CairoSVGConverter)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
