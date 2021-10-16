Welcome to Matplotlib Sphinx Theme's documentation!
===================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This is the official Sphinx theme for Matplotlib documentation. 
It extends the ``pydata_sphinx_theme`` project, but adds custom 
styling and a navigation bar.

When creating a Matplotlib subproject you can include this theme by changing this
line in your conf.py file

.. code-block:: python

   html_theme = 'mpl_sphinx_theme'

And by including ``mpl_sphinx_theme`` as a requirement in your documentation
installation.

Note that the theme does not currently install the `logo2.svg` or 
the `favicon.ico`.  You shoudl copy those from `docs/_static` to 
the local project `docs/_static`.

The full ``conf.py`` is 

.. literalinclude:: conf.py