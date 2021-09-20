import subprocess
from typing import Sequence, Union
from ansi2html import Ansi2HTMLConverter
import click
import git
from git.repo.base import Repo

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command("diff")
@click.option('-p', '--path', type=str, default="./", help='string')
@click.option('-c', '--commit', type=str, default="HEAD")
@click.option('-c2', '--commit2diff', type=str, default="HEAD^")
@click.option('-hp', '--html_path', type=str, default="diff.html")
def diff2html(path: str, commit: str, commit2diff: str, html_path: str):
    click.echo("Diff creation start")
    op = ["git", 'diff', commit2diff, commit, "--color"]
    git = subprocess.run(op, capture_output=True, shell=False, cwd=path)
    diff = git.stdout.decode('utf-8')
    converter = Ansi2HTMLConverter()
    html = converter.convert(diff)
    with open(html_path, "w") as f:
        f.write(html)
    click.echo("Diff creation end")
    
@cli.command("log")
@click.option('-p', '--path', type=str, default="./", help='string')
@click.option('-c', '--commit', type=str, default=None)
@click.option('-a', '--after', type=str, help='example "2021-09-31"')
@click.option('-b', '--before', type=str, help='example "2021-09-31"')
@click.option('-hp', '--html_path', type=str, default="diff.html")
@click.option('-a', "--author", type=str, default=None)
def log2html(path: str, commit: Union[str, None], after: str, before: str, html_path: str, author: Union[str, None]):
    click.echo("diff from log creation start")
    g = git.Repo(path)
    def get_changes(repo: Repo, cmt: Union[str, None], before: str, after: str, author: Union[str, None]) -> Sequence[str]:
        commits = repo.iter_commits(cmt, before=before, after=after, author=author)
        for commit in commits:
            show = repo.git.show(commit)
            yield show
    
    changes = ' '.join(get_changes(g, commit, before, after, author))
    converter = Ansi2HTMLConverter()
    html = converter.convert(changes)
    with open(html_path, "w") as f:
        f.write(html)
    click.echo("diff from log creation end")