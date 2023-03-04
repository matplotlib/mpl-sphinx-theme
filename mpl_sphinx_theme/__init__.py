from ._version import version_info, __version__  # noqa: F401

from pathlib import Path


def set_config_defaults(app):

    try:
        theme = app.builder.theme_options
    except AttributeError:
        theme = None
    if not theme:
        theme = {}

    # Default logo
    logo = theme.get("logo", {})
    if "image_dark" not in logo:
        logo["image_dark"] = "_static/logo_dark.svg"
    if "image_light" not in logo:
        logo["image_light"] = "_static/logo2.svg"
    if "link" not in logo:
        logo["link"] = "https://matplotlib.org/stable/"
    theme["logo"] = logo

    # Update the HTML theme config
    app.builder.theme_options = theme


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
    app.connect("builder-inited", set_config_defaults)
    app.connect("html-page-context", setup_html_page_context)
    return {'version': __version__, 'parallel_read_safe': True}
