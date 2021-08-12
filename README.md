# Python Project Template

This repository serves as a basic python project that can be forked and customised as needed.

## Getting started

### Before you start

Before customising the template you will need to choose a *Short Project Name*, an abbreviated version of the project name suitable for use a python module name (i.e. only letters, no spaces or special characters, see [pep-0008](https://www.python.org/dev/peps/pep-0008/#id40))

### Customising the template

To get started:

1. Fork this repository, and change the name to that of the new project
2. Rename the folder `PROJECTNAME` to the short project name
3. Search for the string `PROJECTNAME` in all the project files and replace with the short name
4. Search for `AUTHORNAME` and replace with the project owners name or email 
5. Remove the forked relationship to the template (optional), this can be done on GitLab under '*Settings*' > '*General*' > '*Advanced Settings*' > '*Remove fork relationship*'
6. Finally customise this README file to describe your project

## Deployment Hooks

For code intended to be deployed you should customise one of the standardised entry point functions:

    train(credentials, parameters)
    validate(credentials, parameters)
    infer(credentials, parameters)

If in doubt, place your code in the `infer()` function.

Credentials will be passed in a dictionary with the structure:

    {
        'System Name':
            {
                'User':'username',
                'Password':'pass'
            },
    }

For example:

    {'ICW':{'User':'u123456', 'Password':'ThePassword123'}}

By default `parameters` will be an empty dictionary, and is reserved for future use.

## Project Structure

The template is based around a standard Python module (see [here](https://docs.python-guide.org/writing/structure/) for details of module structure), and consists of the following:

- `README.md` - This file. Should be customised for the project
- `PROJECTNAME` - Directory containing project code, should be renamed to the project short name
    - `__init__.py` - Defines code that is publicly exposed in the `__all__` variable, customise the docstring to add a high-level overview to the documentation.
    - `infer.py` - Example file containing Python code, may be customised or deleted
	- `train.py` - Example file containing Python code, may be customised or deleted
	- `validate.py` - Example file containing Python code, may be customised or deleted
- `test` - Contains unit test
- `docs` - Contains templates for Sphinx-generated documentation
- `Project Notebook.ipynb` - Example Jupyter notebook for development and running final code
- `setup.py` - Python setuptools config, lists minimum versions of dependencies needed for install, and used to allow stand-alone install of the module
- `requirements.txt` - List exact version of dependencies for unit-testing


## Unit tests

The **test** directory provides a location to place unit tests. 

Tests can be run by opening an anaconda prompt in the **tests** directory and running the command:

    python -m unittest discover

By default the tests will fail unless the template has been properly customised.
