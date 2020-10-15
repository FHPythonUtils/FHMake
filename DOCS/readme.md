Module fhmake
=============
FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
security: Run some basic security checks
publish: Run poetry publish (interactive)
checkreqs: check the requirements file will work with most recent pkg versions
licensechk: check the licences used by the requirements are compatible with this project

Functions
---------

    
`cli()`
:   cli entry point

    
`genRequirements() ‑> NoneType`
:   Generate the requirements files

    
`getDependencies() ‑> dict`
:   Get our dependencies as a dictionary
    
    Returns:
            dict[str, str]: [description]

    
`procVer(version: str, calOnly: bool = False) ‑> str`
:   Process a version string. This is pretty opinionated
    
    Args:
            version (str): the version
    
    Returns:
            str: the processed version

    
`updatePyproject()`
:   Update the pyproject.toml file with our shiny new version specifiers