*************************************
Sphinx SVG to PDF Converter Extension
*************************************

This extension converts SVG images to PDF in case the builder does not support
SVG images natively (e.g. LaTeX).

Internally, either `Inkscape <https://inkscape.org/>`_ or ``rsvg-convert`` from
`libRSVG <https://wiki.gnome.org/Projects/LibRsvg>`_ as a more lightweight
alternative is used to convert images.


Installation
============

Just install via ``pip``:

.. code-block:: console

   $ pip install sphinxcontrib-svg2pdfconverter

You can choose between Inkscape and libRSVG by either adding
``sphinxcontrib.inkscapeconverter`` or ``sphinxcontrib.rsvgconverter`` to the
``extensions`` list in your ``conf.py``.

Make sure to have either ``inkscape`` or the ``rsvg-convert`` command available
in your systems ``PATH`` and, if necessary, adapt the
``inkscape_converter_bin`` or ``rsvg_converter_bin`` config value respectively.


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
