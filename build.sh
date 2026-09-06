#!/usr/bin/env bash

set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Load ShopSphere product/category data
python manage.py loaddata store_data.json

# Create the production Django superuser
# Uses the DJANGO_SUPERUSER_* environment variables from Render
python manage.py createsuperuser --noinput || true