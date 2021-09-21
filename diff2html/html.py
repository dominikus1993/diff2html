from ansi2html import Ansi2HTMLConverter

def convert_and_write(diff: str, html_path: str) -> None: 
    converter = Ansi2HTMLConverter()
    html = converter.convert(diff)
    with open(html_path, "w") as f:
        f.write(html)