from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render
from bookings.models import Booking
from core.models import BlogPost, ContactMessage
from services.models import Category, Service


@staff_member_required
def dashboard_home(request):
    total_users = User.objects.filter(is_staff=False).count()
    total_bookings = Booking.objects.count()
    total_revenue = total_bookings * 120
    pending_jobs = Booking.objects.filter(status='pending').count()
    completed_jobs = Booking.objects.filter(status='completed').count()
    recent_bookings = Booking.objects.select_related('service', 'user').order_by('-created_at')[:6]
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    return render(request, 'dashboard/dashboard_home.html', {
        'total_users': total_users,
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
        'pending_jobs': pending_jobs,
        'completed_jobs': completed_jobs,
        'recent_bookings': recent_bookings,
        'recent_messages': recent_messages,
    })


@staff_member_required
def manage_users(request):
    users = User.objects.filter(is_staff=False).order_by('-date_joined')
    return render(request, 'dashboard/manage_users.html', {'users': users})


@staff_member_required
def manage_bookings(request):
    bookings = Booking.objects.select_related('service', 'user').order_by('-created_at')
    return render(request, 'dashboard/manage_bookings.html', {'bookings': bookings})


@staff_member_required
def manage_services(request):
    services = Service.objects.all().select_related('category')
    categories = Category.objects.all()
    return render(request, 'dashboard/manage_services.html', {
        'services': services,
        'categories': categories,
    })


@staff_member_required
def manage_messages(request):
    messages_list = ContactMessage.objects.order_by('-created_at')
    return render(request, 'dashboard/manage_messages.html', {'messages_list': messages_list})
