#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Crear superusuario usando variables de ambiente
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"mike"}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"miguelpaucar987@gmial.com"}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-"50sombrasdegrey"}

python manage.py createsuperuser --noinput