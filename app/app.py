import subprocess
from ansi2html import Ansi2HTMLConverter
import click

def diff2html(path: str, commit: str, commit2diff: str, html_path: str):
    click.echo("Diff creation start")
    git = subprocess.run(["git", 'diff', commit2diff, commit, "--color"], capture_output=True, shell=False, cwd=path)
    diff = git.stdout.decode('utf-8')
    converter = Ansi2HTMLConverter()
    html = converter.convert(diff)
    with open(html_path, "w") as f:
        f.write(html)
    click.echo("Diff creation end")
