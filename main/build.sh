#!/bin/bash
set -o errexit  # exit on first error

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Apply migrations
python manage.py migrate

# 4. Create superuser if CREATE_SUPERUSER=True
if [ "$CREATE_SUPERUSER" == "True" ]; then
    python - << END
import os
import django
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()
USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME")
EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL")
PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if USERNAME and EMAIL and PASSWORD:
    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD,
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        print(f"Superuser {USERNAME} created successfully.")
    else:
        print(f"Superuser {USERNAME} already exists.")
END
fi
