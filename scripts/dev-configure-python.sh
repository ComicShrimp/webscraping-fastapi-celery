#!/bin/bash

pip install -Iv poetry==1.1.3
pip install --upgrade pip

poetry config virtualenvs.create false
poetry install