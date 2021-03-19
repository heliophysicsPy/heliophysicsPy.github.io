---
layout: page
title: Suggested Python Development Tools
permalink: /docs/suggested_tools/
exclude: true
---
Listed here are tools that PyHC suggests using to aid Python development. The list was compiled by surveying our members about what they use and by independently examining what's popular in industry.

<br>

### IDEs
An IDE, or Integrated Development Environment, enables developers to consolidate the different aspects of writing programs. IDEs increase productivity by combining common activities of writing software into a single application: editing source code, building executables, and debugging. They offer so many conveniences that we recommend using one.

#### [PyCharm](https://www.jetbrains.com/pycharm/)
 * The industry standard for a Python IDE; survey after survey shows that more Python developers use PyCharm than any other alternative
 * Dedicated to Python development, boasting "all the Python tools in one place"
 * Made by Jet Brains, the same people behind the popular IntelliJ IDE, and they offer free and professional options
 * More PyHC respondents reported using PyCharm than any other IDE (21%)

#### [Visual Studio Code](https://code.visualstudio.com)
 * A popular IDE for a variety of languages
 * Support for Python is offered through the [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 * Offered as a free product by Microsoft
 * The secondmost popular IDE among PyHC respondents (18%)

#### [Spyder](https://www.spyder-ide.org) 
 * The Scientific Python Development Environment
 * Designed by and for scientists, written in Python for Python
 * Free and open source, with plugins that extend its functionality
 * 9% of PyHC respondents reported using it

<br>

### Linters
A linter is a basic static code analyzer that checks your source code for programmatic and stylistic errors. They are especially useful for enforcing coding style (like [PEP 8](https://www.python.org/dev/peps/pep-0008/), the style guide all PyHC projects must follow) in projects with multiple developers.

#### [Pylint](https://www.pylint.org) 
 * A thorough Python linter with widespread industry adoption
 * 26% of PyHC respondents use it

#### [Flake8](https://flake8.pycqa.org/en/latest/) 
 * A lightweight alternative to Pylint with comparable industry adoption (arguably more, depending who you ask)
 * 18% of PyHC respondents use it

#### [Black](https://github.com/psf/black) 
 * "The Uncompromising Code Formatter"—_formats_ code instead of just _reporting_ the errors like Pylint and Flake8
 * Very few configuration options to affect the style, meaning code from project to project that is Black formatted looks very similar
 * 6% of PyHC respondents use it

<br>

### Virtual Environment Managers
A Python virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. We recommend using a different virtual environment for every project you work on to avoid dependency compatibility issues—ignoring the default Python installation on your machine altogether.

#### [Anaconda](https://www.anaconda.com) / [Miniconda](https://docs.conda.io/en/latest/miniconda.html) / [Conda](https://docs.conda.io/en/latest/) 
 * Anaconda is the world's most popular Python distribution platform. It includes about a hundred packages, one of which is Conda. It offers a GUI, [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/), that lets you manage Python without using the command line.
 * Miniconda is for the many who consider Anaconda too bloated. It is the smaller alternative to Anaconda that is just Conda and its dependencies.
 * Conda is a package/virtual environment manager, and is the main alternative to [Pip](https://pypi.org/project/pip/). Its benefits include managing virtual environments, not just packages, and checking for dependency compatibility issues before installing new packages.
 * 53% of PyHC respondents use some combination of the three.

#### [Venv](https://docs.python.org/3/library/venv.html) 
 * The go-to virtual environment manager, bundled with Python as of version 3.3
 * Easy to use but lacks more advanced features
 * 12% of PyHC respondents use it

#### [Pyenv](https://github.com/pyenv/pyenv) 
 * Has a more complicated workflow than Venv, but offers more features
 * Makes downloading and installing multiple Python versions easy with its `pyenv install` command
 * 9% of PyHC respondents use it

<br>

### Python Notebooks
Python notebooks are documents that contain live code, equations, visualizations, and/or narrative text all together in one place. They're convenient for sharing code examples and results, among other things.
#### [Jupyter Notebook](https://jupyter.org/#about-notebook) 
 * The go-to Python notebook
 * An open-source web application for creating notebooks
 * 76% of PyHC respondents use it

#### [JupyterLab](https://jupyter.org/#jupyterlab)
 * The next-generation interface for Jupyter notebooks
 * Includes all classic Jupyter Notebook features plus new features
 * Project Jupyter encourages its use
 * 12% (and growing) of PyHC respondents use it

<br>

### Other Tools
Other tools that stand out to us:
 * [ColorOracle](https://colororacle.org)
    * A free color blindness simulator that takes the guesswork out of designing for color blindness by showing you in real time what people with common color vision impairments will see
 * [GitHub Actions](https://github.com/features/actions)
    * We recommend checking out GitHub Actions as an alternative to [TravisCI](https://travis-ci.com), which had been the go-to continuous integration tool for years until it was acquired by Idera and subsequently became expensive
 * [ReadTheDocs](https://readthedocs.org)
    * An excelent documentation tool that automates the building, versioning, and hosting of your docs
 * [pytest](https://docs.pytest.org/en/stable/)
    * The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
 * [coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)
    * A tool for measuring code coverage of Python programs
 * [mypy](http://mypy-lang.org)
    * An optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing

<br>

If you know of a tool we missed that might belong on this page, please contact Shawn Polson at <a href="mailto:Shawn.Polson@lasp.colorado.edu">Shawn.Polson@lasp.colorado.edu</a>.