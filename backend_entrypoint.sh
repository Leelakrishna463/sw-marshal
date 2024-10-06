#!/bin/bash

# Collect Static files
echo "Collecting Static files..."
python manage.py collectstatic --noinput
echo "Finished collecting Static files"

# Apply Database migrations
echo "Applying database migrations..."
python manage.py migrate
echo "Finished applying database migrations"

# Start the server
echo "Starting the server"
python manage.py runserver 0.0.0.0:8000
