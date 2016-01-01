#!/bin/bash

# Step 1. install homebrew
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Step 2. install Python 2.7 via homebrew
brew install python

# Step 3. install git via homebrew
brew install git

# Step 4. fetch the code
git clone https://github.com/joshuakwan/tvshow-scheduler.git

# Step 5. install the prerequisites
cd tvshow-scheduler
pip install -r requirements.txt

# Step 6. launch the app
cd scheduler
python scheduler.py

