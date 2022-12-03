import subprocess
from typing import Union, Union
import click
from git.repo.base import Repo
from diff2html.date import get_first_day_of_month_when_none, get_last_day_of_month_when_none
from diff2html.git import get_changes
from diff2html.output import get_writer 
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command("diff")
@click.option('-p', '--path', type=str, default="./", help='string')
@click.option('-c', '--commit', type=str, default="HEAD")
@click.option('-c2', '--commit2diff', type=str, default="HEAD^")
@click.option('-f', '--filename', type=str, default="diff")
@click.option('-o', "--output", type=click.Choice(["zip", "html"],case_sensitive=True), default="zip")
def diff2html(path: str, commit: str, commit2diff: str, filename: str, output: str):
    click.echo("Diff creation start")
    click.echo("diff from log creation start")
    click.echo("path: {}".format(path))
    click.echo("before: {}".format(commit2diff))
    click.echo("filename: {}".format(filename))
    click.echo("commit: {}".format(commit))
    click.echo("output: {}".format(output))
    op = ["git", 'diff', commit2diff, commit, "--color"]
    git = subprocess.run(op, capture_output=True, shell=False, cwd=path)
    diff = git.stdout.decode('utf-8')
    writer = get_writer(output)
    writer.write(diff, filename)
    click.echo("Diff creation end")

@cli.command("log")
@click.option('-p', '--path', type=str, default="./", help='string')
@click.option('-c', '--commit', type=str, default=None)
@click.option('-a', '--after', type=str, default=None, help='example "2021-09-31"')
@click.option('-b', '--before', type=str, default=None, help='example "2021-09-31"')
@click.option('-f', '--filename', type=str, default="diff")
@click.option('-a', "--author", type=str, default=None)
@click.option('-o', "--output", type=click.Choice(["zip", "html"],case_sensitive=True), default="zip")
def log2html(path: str, commit: Union[str, None], after: Union[str, None], before: Union[str, None], filename: str, author: Union[str, None], output: str):
    before = get_last_day_of_month_when_none(before) if before is None else before
    after = get_first_day_of_month_when_none(after) if after is None else after
    click.echo("diff from log creation start")
    click.echo("path: {}".format(path))
    click.echo("commit: {}".format(commit))
    click.echo("after: {}".format(after))
    click.echo("before: {}".format(before))
    click.echo("filename: {}".format(filename))
    click.echo("author: {}".format(author))
    click.echo("output: {}".format(output))
    g = Repo(path)
    changes = ' '.join(get_changes(g, commit, get_last_day_of_month_when_none(before), get_first_day_of_month_when_none(after), author))
    writer = get_writer(output)
    writer.write(changes, filename)
    click.echo("diff from log creation end")