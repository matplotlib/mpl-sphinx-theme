Matplotlib Sphinx Theme
=======================

This is the official Sphinx theme for Matplotlib documentation.  It extends the
``pydata-sphinx-theme`` project, but adds custom styling and a navigation bar.

A demo of the theme built with the ``main`` branch can be seen at
https://matplotlib.org/mpl-sphinx-theme/.

When creating a Matplotlib subproject you can include this theme by changing this
line in your ``conf.py`` file

.. code-block:: python

   html_theme = 'mpl_sphinx_theme'

And by including ``mpl_sphinx_theme`` as a requirement in your documentation
installation.

See the ``docs/conf.py`` file for other settings.

There are two main templates that replace the defaults in ``pydata-sphinx-theme``:

.. code-block::

   navbar_center = mpl_nav_bar.html
   navbar_end = mpl_icon_links.html

Note that the logo options need not be specified as they are included in theme
initialization. The logo is stored at
``mpl_sphinx_theme/static/logo_{light,dark}.svg``.

To change the top navbar, edit ``mpl_sphinx_theme/mpl_nav_bar.html``

To change the social icons, edit ``mpl_sphinx_theme/mpl_icon_links.html``

To change the style, edit ``mpl_sphinx_theme/static/css/style.css``

Overriding hard coded elements
------------------------------
This theme is primarily designed to be used with subprojects that are part of the main
Matplotlib webiste (e.g., [our cheatseets](https://github.com/matplotlib/cheatsheets]
and [list of third-party packages](https://github.com/matplotlib/mpl-third-party)).
As such several elements are hard coded. However, the theme may also be used by
other subprojects that need to change the hard-coded defaults.
The following sections explain how to reset these back to their defaults by modifying
``html_theme_options`` in ``conf.py``.

Header section links
~~~~~~~~~~~~~~~~~~~~
Use a copy of [the default pydata-sphinx-theme navbar](https://github.com/pydata/pydata-sphinx-theme/blob/main/src/pydata_sphinx_theme/theme/pydata_sphinx_theme/components/navbar-nav.html) and set the ``'navbar_center'`` key to this HTML file in ``html_theme_options``.

Building
--------
To build the theme with a sample page, navigate into the ``doc/`` directory and run

.. code-block::

   make html

The built html pages can be found in ``doc/_build/html/``

Releasing
---------

This project `uses GitHub Actions
<https://github.com/matplotlib/mpl-sphinx-theme/blob/main/.github/workflows/release.yml>`_
to automatically push a new release to PyPI whenever a release is made.

For example, to release a new ``3.9.0`` version of ``mpl-sphinx-theme``:

- be sure to edit `mpl_sphinx_theme/_version.py`
- checkout the commit you would like to release
- add a git tag
- push the tag to the ``matplotlib/mpl-sphinx-theme`` repository

.. code-block::

   $ git checkout <commit-hash>
   $ git tag -s -a v3.9.0 -m 'REL: 3.9.0'
   $ git push upstream --tags

Finally, `turn the tag into a GitHub release
<https://github.com/matplotlib/mpl-sphinx-theme/releases/new>`_.

Update the required ``mpl-sphinx-theme`` version in the following files:

* matplotlib/matplotlib: requirements/doc/doc-requirements.txt
* matplotlib/mpl-brochure-site: requirements.txt
* matplotlib/mpl-third-party: docs/requirements.txt
* matplotlib/governance: requirements-doc.txt
* matplotlib/mpl-gui: requirements-doc.txt
