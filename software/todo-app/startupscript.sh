#!/bin/bash

python3 -m venv /home
source /home/bin/activate
pip install -r requirements.txt

python3 DataBase.py
python3 main.py


