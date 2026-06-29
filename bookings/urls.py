from django.urls import path
from . import views

urlpatterns = [
    path('new/<slug:slug>/', views.create_booking, name='create-booking'),
    path('history/', views.booking_history, name='booking-history'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel-booking'),
]