import subprocess
from ansi2html import Ansi2HTMLConverter
import argparse


parser = argparse.ArgumentParser(description='Create diff from two commits.')

parser.add_argument('--path', metavar='N', default="./", type=str, help='string')
parser.add_argument('--commit', metavar='N', default="HEAD", type=str, help='string')
parser.add_argument('--commit2diff', metavar='N', type=str, help='string')                    
parser.add_argument('--htmlpath', metavar='N', default="diff.html", type=str, help='string')   

args = parser.parse_args()

def get_diff(path: str = "./", commit: str = "HEAD", commit2diff: str = "HEAD^") -> str:
    git = subprocess.run(["git", 'diff', commit2diff, commit, "--color"], capture_output=True, shell=False, cwd=path)
    return git.stdout.decode('utf-8')

def save_diff_as_html(text: str, html_path: str):
    converter = Ansi2HTMLConverter()
    html = converter.convert(text)
    with open(html_path, "w") as f:
        f.write(html)

diff = get_diff(args.path, args.commit, args.commit2diff)

save_diff_as_html(diff, args.htmlpath)