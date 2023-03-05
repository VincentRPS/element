"""
MIT License

Copyright (c) 2023 VincentRPS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from .._about import __version__
from ..pyproject import ConfigV1
from pathlib import Path
from ._build_wheel_requires import get_requirements


def build_metadata(path: Path, config: ConfigV1) -> None:
    path.write_text(u'Metadata-Version: 2.1\n')
    path.write_text(u'Name: {name}\n'.format(name=config.mod.name))
    path.write_text(u'Version: {version}\n'.format(version=config.mod.version))
    path.write_text(u'Author: {author}\n'.format(author=config.mod.author))

    for classifier in config.mod.classifiers:
        path.write_text(u'Classifier: {classifier}\n'.format(classifier=classifier))

    if config.mod.description:
        path.write_text(u'Summary: {summary}\n'.format(summary=config.mod.description))

    if config.mod.author_email:
        path.write_text(u'Author-email: {author_email}\n'.format(author_email=config.mod.author_email))

    if config.mod.homepage:
        path.write_text(u'Home-page: {homepage}\n'.format(homepage=config.mod.homepage))

    if config.mod.license:
        path.write_text(u'License: {license}\n'.format(config.mod.license))

    path.write_text(u'Keywords: {keywords}\n'.format(keywords=' '.join(config.mod.keywords)))

    if config.mod.maintainer:
        path.write_text(u'Maintainer: {maintainer}\n'.format(maintainer=config.mod.maintainer))

    if config.mod.maintainer_email:
        path.write_text(u'Maintainer-email: {maintainer_email}\n'.format(maintainer=config.mod.maintainer_email))

    if config.mod.python:
        path.write_text(u'Requires-Python: {python}\n'.format(python=config.mod.python))

    if config.mod.readme:
        path.write_text(u'Description: {description}\n'.format(description=Path(config.mod.readme).open().read()))

    if config.mod.readme_type:
        path.write_text(u'Description-Content-Type: {content_type}\n'.format(content_type=config.mod.readme_type))

    for name_url, url in config.urls.items():
        path.write_text(u'Project-URL: {name_url}, {url}\n'.format(name_url=name_url, url=url))

    requires = get_requirements()

    for require in requires:
        path.write_text(u'Requires-Dist: {dist}\n'.format(dist=require))

    if config.mod.documentation:
        path.write_text(u'Project-URL: Documentation, {doc}\n'.format(config.mod.documentation))

    if config.mod.repository:
        path.write_text(u'Project-URL: Repository, {rep}\n'.format(config.mod.repository))