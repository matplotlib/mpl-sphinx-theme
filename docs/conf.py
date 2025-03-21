import os
import time
import datetime
import matplotlib  # noqa: F401
# Configuration file for the Sphinx documentation builder for
# matplotlib projects.

# Release mode enables optimizations and other related options.
is_release_build = tags.has('release')  # noqa

# Parse year using SOURCE_DATE_EPOCH, falling back to current time.
# https://reproducible-builds.org/specs/source-date-epoch/
build_date = datetime.datetime.utcfromtimestamp(
    int(os.environ.get('SOURCE_DATE_EPOCH', time.time()))
)

# -- Project information -----------------------------------------------------

project = "Matplotlib Sphinx Theme"
copyright = (
    f"2012 - {build_date.year} The Matplotlib development team"
)
author = "Matplotlib Developers"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'matplotlib.sphinxext.plot_directive',
]

# Add any paths that contain templates here, relative to this directory.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "mpl_sphinx_theme"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    # logo is installed by mpl-sphinx-theme as:
    # "logo": {"link": "https://matplotlib.org/stable/",
    #         "image_light": "_static/logo_light.svg",
    #         "image_dark": "_static/logo_dark.svg"},
    # if this default is OK, then no need to modify "logo"
    # collapse_navigation in pydata-sphinx-theme is slow, so skipped for local
    # and CI builds https://github.com/pydata/pydata-sphinx-theme/pull/386
    "collapse_navigation": not is_release_build,
    "show_prev_next": False,
    # Determines the type of links produced in the navigation header:
    # - absolute: Links point to the URL https://matplotlib.org/...
    # - server-stable: Links point to top-level of the server /stable/...
    # - internal: Links point to the internal files as expanded by the `pathto`
    #   template function in Sphinx.
    "navbar_links": "absolute",
}

html_sidebars = {
    "index": [
        "donate_sidebar.html",
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
