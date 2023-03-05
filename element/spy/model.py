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
import msgspec


class _Package(msgspec.Struct):
    include: str
    where: str


class _Include(msgspec.Struct):
    path: str
    format: str


class PackageConfig(msgspec.Struct):
    name: str
    version: str
    description: str
    author: str
    python: str | None = None
    author_email: str | None = None
    homepage: str | None = None
    repository: str | None = None
    documentation: str | None = None
    maintainer: str | None = None
    maintainer_email: str | None = None
    license: str | None = None
    readme: str | None = None
    readme_type: str | None = None
    keywords: list[str] = []
    auto_find_package: bool = True
    packages: list[_Package | str] | None = None
    include: _Include = []
    exclude: list[str] = []
    classifiers: list[str] = []


class DependencyLock(msgspec.Struct):
    version: str
    python: str | None = None


class Script(msgspec.Struct):
    cmd: str
    extra: str


class ConfigV1(msgspec.Struct):
    mod: PackageConfig
    dependencies: dict[str, str] | dict[str, DependencyLock] = {}
    extras: dict[str, list[str]] | dict[str, DependencyLock] = {}
    scripts: dict[str, str | Script] = {}
    urls: dict[str, str] = {}
