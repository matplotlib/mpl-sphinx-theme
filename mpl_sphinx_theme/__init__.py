from ._version import version_info, __version__  # noqa: F401

from pathlib import Path


def get_html_theme_path():
    """Return list of HTML theme paths."""
    return [str(Path(__file__).parent.parent.resolve())]


def setup_html_page_context(app, pagename, templatename, context, doctree):
    """Add a mpl_path template function."""
    navbar_links = context['theme_navbar_links']
    if navbar_links not in ['internal', 'absolute', 'server-stable']:
        raise ValueError(f'Invalid navbar_links theme option: {navbar_links}')

    def mpl_path(path):
        if navbar_links == 'internal':
            pathto = context['pathto']
            return pathto(path)
        elif navbar_links == 'absolute':
            return f'https://matplotlib.org/stable/{path}'
        elif navbar_links == 'server-stable':
            return f'/stable/{path}'
        else:
            raise ValueError(
                f'Invalid navbar_links theme option: {navbar_links}')
    context['mpl_path'] = mpl_path


# For more details, see:
# https://www.sphinx-doc.org/en/master/development/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    here = Path(__file__).parent.resolve()
    # Include component templates
    app.config.templates_path.append(str(here / "components"))

    app.add_html_theme("mpl_sphinx_theme", str(here))
    app.connect("html-page-context", setup_html_page_context)
    return {'version': __version__, 'parallel_read_safe': True}
