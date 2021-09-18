import subprocess
from ansi2html import Ansi2HTMLConverter

git = subprocess.run(["git", 'diff', "dadd78463431798db69b1452a7e8c159743cc7ed", 'HEAD', "--color"], capture_output=True, shell=False)

conv = Ansi2HTMLConverter()

ansi = git.stdout.decode('utf-8')

html = conv.convert(ansi)

f = open("xd.html", "w")
f.write(html)