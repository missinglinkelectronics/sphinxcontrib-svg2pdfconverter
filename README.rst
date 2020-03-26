*************************************
Sphinx SVG to PDF Converter Extension
*************************************

This extension converts SVG images to PDF in case the builder does not support
SVG images natively (e.g. LaTeX).

Internally, either `Inkscape <https://inkscape.org/>`_, ``rsvg-convert``
from `libRSVG <https://wiki.gnome.org/Projects/LibRsvg>`_ or `CairoSVG
<https://cairosvg.org/>`_ as progressively more lightweight alternatives
are used to convert images.


Installation
============

Just install via ``pip``:

.. code-block:: console

   $ pip install sphinxcontrib-svg2pdfconverter

You can choose between Inkscape, libRSVG and CairoSVG by adding
``sphinxcontrib.inkscapeconverter``, ``sphinxcontrib.rsvgconverter`` or
``sphinxcontrib.cairosvgconverter`` to the ``extensions`` list in your
``conf.py``.

Make sure to have either ``inkscape`` or the ``rsvg-convert`` command available
in your systems ``PATH`` and, if necessary, adapt the
``inkscape_converter_bin`` or ``rsvg_converter_bin`` config value respectively.

``CairoSVG`` has extra dependency requiring install with ``CairoSVG`` extra:

.. code-block:: console

   $ pip install sphinxcontrib-svg2pdfconverter[CairoSVG]

It also needs native libraries that must be installed according to
operating system used. See the `CairoSVG documentation
<https://cairosvg.org/documentation/>`_ for details.

Configuration
=============

Inkscape
--------

``inkscape_converter_bin``
    Path to Inkscape binary. By default, this is ``inkscape``.

``inkscape_converter_args``
    Additional command-line arguments for Inkscape, as a list. By
    default, this is ``['--export-area-drawing']``.

RSVG
----

``rsvg_converter_bin``
    Path to RSVG converter binary. By default, this is ``rsvg-convert``.

``rsvg_converter_args``
    Additional command-line arguments for the RSVG converter, as a list. By
    default, this is the emtpy list ``[]``.

CairoSVG
--------

No configuration is required.
