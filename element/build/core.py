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

from pathlib import Path
from element import pyproject

from .._about import __version__
from ._build_wheel_requires import get_requirements
from ._metadata_builder import build_metadata


pyproject_toml = Path('pyproject.toml')


get_requires_for_build_wheel = get_requirements
get_requires_for_build_sdist = get_requirements
get_requires_for_build_editable = get_requirements


wheel_file_template = u"""\
Wheel-Version: 1.0
Generator: element {version}
Root-Is-Purelib: true
Tag: py3-none-any
""".format(version=__version__)


def prepare_metadata_for_build_wheel(metadata_directory: str, config_settings=None) -> str:
    config = pyproject.load(pyproject_toml)

    path = Path(f'{metadata_directory}/{config.mod.name}-{config.mod.version}.dist-info')
    if path.exists():
        path.rmdir()
    path.mkdir()

    wheel_path = path.joinpath('WHEEL')
    metadata_path = path.joinpath('METADATA')
    wheel_path.touch()
    metadata_path.touch()

    wheel_path.write_text(wheel_file_template, 'utf-8')
    build_metadata(metadata_path, config)

    return str(path)


prepare_metadata_for_build_editable = prepare_metadata_for_build_wheel



