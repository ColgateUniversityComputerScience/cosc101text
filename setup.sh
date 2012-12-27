#!/bin/bash

curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py
python virtualenv.py pyenv
. ./pyenv/bin/activate
pip install sphinx
