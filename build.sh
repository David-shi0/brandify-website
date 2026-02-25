#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating static directories..."
mkdir -p staticfiles
mkdir -p static
mkdir -p core/static

echo "Collecting static files..."
python manage.py collectstatic --no-input --settings=render_settings

echo "Running migrations..."
python manage.py migrate --settings=render_settings

echo "Build completed!"
