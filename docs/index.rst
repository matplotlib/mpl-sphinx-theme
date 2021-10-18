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

There are three main templates that replace the defaults in ``pydata-sphinx-theme``:

.. code-block::

   navbar_start = mpl_navbar_logo.html
   navbar_center = mpl_nav_bar.html
   navbar_end = mpl_icon_links.html   

Note that the option ``html_logo`` need not be specified as it is included 
in ``mpl_sphinx_theme/mpl_navbar_logo.html``.  The logo is stored at 
``mpl_sphinx_theme/static/images/logo2.svg``.  

To change the top navbar, edit ``mpl_sphinx_theme/mpl_nav_bar.html``

To change the social icons, edit ``mpl_sphinx_theme/mpl_icon_links.html``

To change the style, edit ``mpl_sphinx_theme/static/css/style.css``

The full ``conf.py`` is 

.. literalinclude:: conf.py