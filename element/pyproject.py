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
import pathlib
import tomllib

import msgspec

from .errors import PyProjectError

from .spy.model import ConfigV1, PackageConfig


def load(path: pathlib.Path) -> ConfigV1:
    if not path.exists():
        raise PyProjectError('pyproject.toml does not exist')

    if not path.is_file():
        raise PyProjectError('pyproject.toml must be a file')

    contents = path.open().read()
    parsed = tomllib.loads(contents)

    try:
        tool = parsed['tool']['element']
        edition = parsed['edition']
    except KeyError:
        raise PyProjectError('[tool.element] or edition does not exist on pyproject.toml')

    if edition == '2023.0.0':
        cfg = ConfigV1
    else:
        raise PyProjectError(f'Edition picked ({edition}) is invalid')

    try:
        mod = PackageConfig(**tool['mod'])
        config = cfg(mod=mod, dependencies=tool.get('dependencies', {}), extras=tool.get('extras', {}), scripts=tool.get('scripts', {}), urls=tool.get('urls', {}))
    except msgspec.ValidationError as e:
        raise PyProjectError('Validation error with pyproject.toml occured.\n\n', e)


    return config
