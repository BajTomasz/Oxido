#!/bin/bash

python -m  venv .venv   
source .venv/bin/activate
pip install -r requirements.txt
touch config.json
python -m main
deactivate