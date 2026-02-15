#!/bin/bash
python manage.py migrate

# Auto-create superuser if doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.filter(username='admin').exists() or User.objects.create_superuser('anonymous', 'admin@example.com', '123@')
"
python manage.py runserver 0.0.0.0:8000