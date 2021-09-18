import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = "diff2html",
    version = "1.0.0",
    author = "Dominik Kotecki",
    author_email = "dominikus1910@gmail.com",
    description = ("Prints git diff to html"),
    license = "MIT",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    py_modules =['diff2html', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    entry_points = '''
        [console_scripts]
        diff2html=diff2html:cli
    '''
)