
# create a new project with toml file
poetry new my_stuff

# work from project
cd my-stuff
poetry add pandas --lock  

# create requirements file
poetry self add poetry-plugin-export  # call once
poetry export -f requirements.txt --output requirements.txt
poetry config warnings.export false  # did not seem to make warning go away


# do not use update as it also install, use poetry lock in stead
# pip will take care of installation
poetry lock # update lock 

# install to e.g. here
pip install -r requirements.txt --target="./site-packages"

#note add to .vscode/settings.json to help pylance
# "python.analysis.extraPaths": [ 
#     "./my-stuff/site-packages"
# ]


# add to any python script to make sure local packages are in scope
# add local packages to path
import sys
sys.path.append("./site-packages")


# https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators
brew tap azure/functions
brew install azure-functions-core-tools@4

func init --python


# Customer packages not in sys path.
https://stackoverflow.com/questions/77479584/local-azure-function-customer-packages-not-in-sys-path-this-should-never-happe