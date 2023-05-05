#!/bin/bash

# CONDA:
# 1) The initial bash command included activating Conda as well.
# 2) During testing, we realized that this was not practical since not all users had Conda installed or joined to path.
# 3) We recommend installing Conda and running the commands independently, as indicated in the README.md file.

# This program runs the ifi_terminal program without navigating to src.

# Note: To run this code, use 'bash ifi_terminal' instead of granting execute access, which may not work consistently on all devices. It's easier to run using 'bash ifi_terminal.sh'.

# Navigate to the src directory and run main.py.
echo "Running ifi_terminal..."
cd src
python3 main.py
