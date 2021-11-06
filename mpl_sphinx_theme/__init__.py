from ._version import version_info, __version__  # noqa: F401

from pathlib import Path


def get_html_theme_path():
    """Return list of HTML theme paths."""
    return [str(Path(__file__).parent.parent.resolve())]


# For more details, see:
# https://www.sphinx-doc.org/en/master/development/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme("mpl_sphinx_theme",
                       str(Path(__file__).parent.resolve()))
