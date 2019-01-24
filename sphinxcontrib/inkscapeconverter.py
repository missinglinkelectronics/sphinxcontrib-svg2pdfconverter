# -*- coding: utf-8 -*-
"""
    sphinxcontrib.inkscapeconverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Converts SVG images to PDF using Inkscape in case the builder does not
    support SVG images natively (e.g. LaTeX).

    :copyright: Copyright 2018 by Missing Link Electronics, Inc.
    :license: BSD, see LICENSE for details.
"""
import subprocess

from sphinx.errors import ExtensionError
from sphinx.locale import __
from sphinx.transforms.post_transforms.images import ImageConverter
from sphinx.util import logging
from sphinx.util.osutil import ENOENT, EPIPE, EINVAL

if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA


logger = logging.getLogger(__name__)


class InkscapeConverter(ImageConverter):
    conversion_rules = [
        ('image/svg+xml', 'application/pdf'),
    ]

    def is_available(self):
        # type: () -> bool
        """Confirms if Inkscape is available or not."""
        try:
            args = [self.config.inkscape_converter_bin, '--version']
            logger.debug('Invoking %r ...', args)
            ret = subprocess.call(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            if ret == 0:
                return True
            else:
                return False
        except (OSError, IOError):
            logger.warning(__('Inkscape command %r cannot be run. '
                              'Check the inkscape_converter_bin setting'),
                           self.config.inkscape_converter_bin)
            return False

    def convert(self, _from, _to):
        # type: (unicode, unicode) -> bool
        """Converts the image from SVG to PDF via Inkscape."""
        try:
            args = ([self.config.inkscape_converter_bin] +
                    self.config.inkscape_converter_args +
                    ['--export-pdf=' + _to, _from])
            logger.debug('Invoking %r ...', args)
            p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        except OSError as err:
            if err.errno != ENOENT:  # No such file or directory
                raise
            logger.warning(__('Inkscape command %r cannot be run. '
                              'Check the inkscape_converter_bin setting'),
                           self.config.inkscape_converter_bin)
            return False

        try:
            stdout, stderr = p.communicate()
        except (OSError, IOError) as err:
            if err.errno not in (EPIPE, EINVAL):
                raise
            stdout, stderr = p.stdout.read(), p.stderr.read()
            p.wait()
        if p.returncode != 0:
            raise ExtensionError(__('Inkscape exited with error:\n'
                                    '[stderr]\n%s\n[stdout]\n%s') %
                                 (stderr, stdout))

        return True


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
