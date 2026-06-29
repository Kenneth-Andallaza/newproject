from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard-home'),
    path('users/', views.manage_users, name='dashboard-users'),
    path('bookings/', views.manage_bookings, name='dashboard-bookings'),
    path('services/', views.manage_services, name='dashboard-services'),
    path('messages/', views.manage_messages, name='dashboard-messages'),
]