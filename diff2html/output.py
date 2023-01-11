

import abc
import os
import zipfile

from ansi2html import Ansi2HTMLConverter

from diff2html.files import write_force, write_zip_force

class DiffWriter(abc.ABC):

    @abc.abstractmethod
    def write(self, diff: str, filename: str) -> None:
        pass

class HtmlDiffWriter(DiffWriter):
    
    def write(self, diff: str, filename: str) -> None:
        html_path = f'{filename}.html'
        converter = Ansi2HTMLConverter()
        html = converter.convert(diff)
        write_force(html_path, html)

class ZipDiffWriter(DiffWriter):

    htmL_writer: HtmlDiffWriter
    
    def __init__(self, htmL_writer: HtmlDiffWriter) -> None:
        self.htmL_writer = htmL_writer
        super().__init__()
    
    def write(self, diff: str, filename: str) -> None:
        html_path = f'{filename}.html'
        zip_path = f'{filename}.zip'
        self.htmL_writer.write(diff, filename)
        write_zip_force(zip_path, html_path)


def get_writer(output_type: str) -> DiffWriter:
    if output_type == "zip":
        return ZipDiffWriter(HtmlDiffWriter())
    elif output_type == "html":
        return HtmlDiffWriter()
    raise ValueError(f"Unknown output type: {output_type}")