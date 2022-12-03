

import abc
import os
import zipfile

from ansi2html import Ansi2HTMLConverter

from diff2html.files import write_force, write_zip_force


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
        write_force(html_path, html)
        write_zip_force(zip_path, html_path)
        os.remove(html_path)

class HtmlDiffWriter(DiffWriter):
    
    def write(self, diff: str, filename: str) -> None:
        html_path = f'{filename}.html'
        converter = Ansi2HTMLConverter()
        html = converter.convert(diff)
        write_force(html_path, html)

def get_writer(output_type: str) -> DiffWriter:
    if output_type == "zip":
        return ZipDiffWriter()
    elif output_type == "html":
        return HtmlDiffWriter()
    raise ValueError(f"Unknown output type: {output_type}")