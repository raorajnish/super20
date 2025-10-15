#!/bin/bash

# Exit on any error
set -e

echo "Starting Django application setup..."

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Create superuser (will skip if already exists)
echo "Creating superuser..."
python manage.py create_superuser

# Start the application
echo "Starting Django application..."
python manage.py runserver 0.0.0.0:$PORT
