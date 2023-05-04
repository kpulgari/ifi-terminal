#!/bin/bash

# CONDA:
# 1) Initiall bash command included activating conda as well
# 2) On Testing we realised that this was not practical since all users did not have conda installed or joined to path
# 3) We recommend installing conda and running the commands indipendently as indicated in the README.md file


# Program to run the ifi_terminal program...without navigating to src

# navigate into src directory and run main.py
echo "Running ifi_terminal program..."
cd src
python3 main.py


# Note: using 'bash ifi_terminal to run this code, since granting execute access may not run the same on all devices depending on setting. User would have to use sudo.. Much easier to run using bash ifi_terminal.sh'