from core.html import convert_and_write
import subprocess
from typing import Sequence, Union
from ansi2html import Ansi2HTMLConverter
import click
from core.git import get_changes
from git.repo.base import Repo
from core.date import get_first_day_of_month_when_none, get_last_day_of_month_when_none 
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
    click.echo("diff from log creation start")
    click.echo("path: {}".format(path))
    click.echo("before: {}".format(commit2diff))
    click.echo("html_path: {}".format(html_path))
    op = ["git", 'diff', commit2diff, commit, "--color"]
    git = subprocess.run(op, capture_output=True, shell=False, cwd=path)
    diff = git.stdout.decode('utf-8')
    convert_and_write(diff, html_path)
    click.echo("Diff creation end")

@cli.command("log")
@click.option('-p', '--path', type=str, default="./", help='string')
@click.option('-c', '--commit', type=str, default=None)
@click.option('-a', '--after', type=str, default=None, help='example "2021-09-31"')
@click.option('-b', '--before', type=str, default=None, help='example "2021-09-31"')
@click.option('-hp', '--html_path', type=str, default="diff.html")
@click.option('-a', "--author", type=str, default=None)
def log2html(path: str, commit: Union[str, None], after: Union[str, None], before: Union[str, None], html_path: str, author: Union[str, None]):
    before = get_last_day_of_month_when_none(before) if before is None else before
    after = get_first_day_of_month_when_none(after) if after is None else after
    click.echo("diff from log creation start")
    click.echo("path: {}".format(path))
    click.echo("commit: {}".format(commit))
    click.echo("after: {}".format(after))
    click.echo("before: {}".format(before))
    click.echo("html_path: {}".format(html_path))
    click.echo("author: {}".format(author))
    g = Repo(path)
    changes = ' '.join(get_changes(g, commit, get_last_day_of_month_when_none(before), get_first_day_of_month_when_none(after), author))
    convert_and_write(changes, html_path)
    click.echo("diff from log creation end")