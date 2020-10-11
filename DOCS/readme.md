Module fhmake
=============
FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
security: Run some basic security checks that are not run in vscode
publish: Run poetry publish
checkreqs: check our requirements file will work with most recent pkg versions

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

    
`procVer(version: str) ‑> str`
:   Process a version string
    
    Args:
            version (str): the version
    
    Returns:
            str: the processed version