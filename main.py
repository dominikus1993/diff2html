import subprocess
from typing import Union
from ansi2html import Ansi2HTMLConverter
import git 

g = git.Repo('./')

commits = g.iter_commits("HEAD", before="2021-09-31", after="2021-09-1'", author="")
# hexshas = g.log("--before='2021-09-31'",  "--after='2021-08-1'").split('\n') 

for commit in commits:
    print(commit.)