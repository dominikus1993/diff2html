import subprocess

git = subprocess.run(["git", 'diff', "dadd78463431798db69b1452a7e8c159743cc7ed", 'HEAD', "--color"])

print(git.stdout.decode('utf-8'))

