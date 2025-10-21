from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('request/new/', views.new_request_view, name='new_request'),
]
