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

Note that the option ``html_logo`` need not be specified as it is for 
``pydata-sphinx-theme``.

To change the top navbar, edit ``mpl_sphinx_theme/mpl_nav_bar.html``

The full ``conf.py`` is 

.. literalinclude:: conf.py