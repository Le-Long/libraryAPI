#!/usr/bin/env bash
set -o errexit

poetry install

python manage.py collecstatic --no-input
python manage.py migrate
