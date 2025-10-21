from django.contrib import admin
from django.urls import path, include

# acit_portal/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),  # The Admin is accessible at /admin/
    path('', include('requests_app.urls')), # The requests app is at the root /
]
