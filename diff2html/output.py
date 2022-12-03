

import abc
import os
import zipfile

from ansi2html import Ansi2HTMLConverter


class DiffWriter(abc.ABC):

    @abc.abstractmethod
    def write(self, diff: str, filename: str) -> None:
        pass

class ZipDiffWriter(DiffWriter):

    def write(self, diff: str, filename: str) -> None:
        html_path = f'{filename}.html'
        zip_path = f'{filename}.zip'
        converter = Ansi2HTMLConverter()
        html = converter.convert(diff)
        with open(html_path, "w") as f:
            f.write(html)
        with zipfile.ZipFile(zip_path, 'a') as zf:
            zf.write(html_path, os.path.basename(html_path))
        os.remove(html_path)

class HtmlDiffWriter(DiffWriter):

    def write(self, diff: str, filename: str) -> None:
        html_path = f'{filename}.html'
        converter = Ansi2HTMLConverter()
        html = converter.convert(diff)
        with open(html_path, "w") as f:
            f.write(html)  

def get_writer(output_type: str) -> DiffWriter:
    if output_type == "zip":
        return ZipDiffWriter()
    elif output_type == "html":
        return HtmlDiffWriter()
    raise ValueError(f"Unknown output type: {output_type}")