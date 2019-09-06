#!/bin/bash
pyenv local 3.6.0
virtualenv virtenv-python3.6
source virtenv-python3.6/bin/activate
pip install "django<2"
pip install selenium
