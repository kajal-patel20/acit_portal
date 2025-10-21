import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acit_portal.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@acitportal.com',
        password='admin123'  # Change this after first login!
    )
    print("✅ Superuser created: username='admin', password='admin123'")
else:
    print("ℹ️ Superuser 'admin' already exists")
