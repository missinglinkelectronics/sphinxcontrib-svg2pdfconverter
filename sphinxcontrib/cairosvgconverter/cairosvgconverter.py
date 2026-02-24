# -*- coding: utf-8 -*-
# SPDX-License-Indentifier: BSD-2-Clause
# Copyright (C) 2018-2023 Stefan Wiehler <sphinx_contribute@missinglinkelectronics.com>
# Copyright (C) 2020 by Marko Kohtala <marko.kohtala@gmail.com>
from sphinx.errors import ExtensionError
from sphinx.locale import __
from sphinx.transforms.post_transforms.images import ImageConverter
from sphinx.util import logging
from urllib.error import URLError

if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA


logger = logging.getLogger(__name__)


class CairoSVGConverter(ImageConverter):
    conversion_rules = [
        ('image/svg+xml', 'application/pdf'),
        ('image/svg+xml', 'image/png'),
    ]

    def is_available(self):
        # type: () -> bool
        """Confirms if CairoSVG package is available or not."""
        try:
            import cairosvg  # noqa: F401
            return True
        except ImportError:
            logger.warning(__('CairoSVG package cannot be imported. '
                              'Check if CairoSVG has been installed properly'))
            return False

    def convert(self, _from, _to):
        # type: (unicode, unicode) -> bool
        """Converts the image from SVG to PDF or PNG via CairoSVG."""
        import cairosvg
        import pathlib
        try:
            # Guess output format based on file extension
            fmt = pathlib.Path(str(_to)).suffix[1:]
            if fmt == 'png':
                cairosvg.svg2png(file_obj=open(_from, 'rb'), write_to=_to)
            else:
                cairosvg.svg2pdf(file_obj=open(_from, 'rb'), write_to=_to)
        except (OSError, URLError) as err:
            raise ExtensionError(__('CairoSVG converter failed with reason: '
                                    '%s') % err.reason)

        return True
