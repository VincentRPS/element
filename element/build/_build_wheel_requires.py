from pathlib import Path
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
from typing import Any
from .. import pyproject
from packaging.requirements import Requirement, InvalidRequirement
from ..errors import ElementError


pyproject_toml = Path('pyproject.toml')


def get_requirements(config_settings: Any | None = None) -> list[str]:
    config = pyproject.load(pyproject_toml)

    requirements: list[str] = []

    for name, value in config.dependencies.items():
        if isinstance(value, str):
            # TODO: support other pythonic requirement types
            if value.startswith('^'):
                req = name + '~=' + value.removeprefix('^')
            else:
                req = name + '==' + value

            requirements.append(req)
        else:
            version = value.version

            if version.startswith('^'):
                req = name + '~=' + version.removeprefix('^')

                if value.python:
                    req += f'; python_version {value.python}'
            else:
                req = name + '==' + version

                if value.python:
                    req += f'; python_version {value.python}'

            try:
                Requirement(req)
            except InvalidRequirement:
                raise ElementError(f'Requirement given ({req}) is not valid')

            requirements.append(req)

    return requirements
