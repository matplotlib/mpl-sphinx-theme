#!/usr/bin/env python

from setuptools import setup
import mpl_sphinx_theme

setup(
    name="mpl_sphinx_theme",
    version=mpl_sphinx_theme.__version__,
    url="https://github.com/matplotlib/mpl-sphinx-theme",
    license="BSD",
    author="Matplotlib Developers",
    description="Matplotlib theme for Sphinx",
    long_description=open("README.rst").read(),
    zip_safe=False,
    packages=["mpl_sphinx_theme"],
    package_data={
        "mpl_sphinx_theme": [
            "theme.conf",
            "*.html",
            "static/css/*.css",
            "static/images/*.svg",
            "static/images/*.ico",
            "static/js/*.js",
            "static/font/*.*",
            "components/*.html",
        ]
    },
    include_package_data=True,
    # http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        "sphinx.html_themes": [
            "mpl_sphinx_theme = mpl_sphinx_theme",
        ]
    },
    install_requires=open("requirements.txt").read().strip().split("\n"),
)
