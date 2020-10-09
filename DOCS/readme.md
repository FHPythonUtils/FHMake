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

    
`genRequirements()`
:   

    
`procVer(version: str) ‑> str`
: