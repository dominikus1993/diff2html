from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = "diff2html",
    version = "1.1.0",
    author = "Dominik Kotecki",
    author_email = "dominikus1910@gmail.com",
    description = ("Prints git diff to html"),
    license = "MIT",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    py_modules =['diff2html'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    entry_points = '''
        [console_scripts]
        diff2html=diff2html.cli:cli
    '''
)
