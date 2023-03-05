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
# builds wheels

from pathlib import Path
import tempfile
import zipfile

from ..errors import ElementError
from ..spy.model import ConfigV1
from ._metadata_builder import build_metadata


def get_submodules(mod: Path) -> list[str]:
    if not mod.exists():
        raise ElementError('Module path must exist')

    submodules = []

    for path in mod.glob('**/**'):
        if not path.is_file():
            submodules.append(str(path).replace('\\', '.').replace('/', '.'))

    return submodules


class WheelConstructor:
    def __init__(self, config: ConfigV1, target: str) -> None:
        self._config = config
        self._temp_dir = Path(tempfile.mkdtemp(prefix='element.wheel.'))
        self.zip = zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED)
        try:
            build_metadata(self._temp_dir, config)
        except:
            self._temp_dir.unlink(True)
            raise
