from django.contrib import messages
from django.shortcuts import redirect, render
from bookings.models import Booking
from services.models import Category, Service
from .forms import ContactForm
from .models import BlogPost


def home(request):
    categories = Category.objects.all()[:8]
    popular_services = Service.objects.filter(is_featured=True)[:6]
    testimonials = [
        {
            'name': 'Sophia Khan',
            'role': 'Homeowner',
            'message': 'ServiceHub made booking a technician so easy and fast. Highly recommended!',
        },
        {
            'name': 'Mark Davis',
            'role': 'Apartment Owner',
            'message': 'The professionals are trusted, punctual and deliver excellent service every time.',
        },
    ]
    stats = {
        'bookings': Booking.objects.count(),
        'professionals': Service.objects.count(),
        'customers': Category.objects.count() * 120,
        'reviews': 320,
    }
    latest_blogs = BlogPost.objects.filter(is_published=True)[:3]
    return render(request, 'core/home.html', {
        'categories': categories,
        'popular_services': popular_services,
        'testimonials': testimonials,
        'stats': stats,
        'latest_blogs': latest_blogs,
    })


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your message has been sent. Our team will get back to you soon.')
        return redirect('contact')
    return render(request, 'core/contact.html', {'form': form})


def faq(request):
    return render(request, 'core/faq.html')


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)[:6]
    return render(request, 'core/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = BlogPost.objects.filter(is_published=True).get(slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})


def page_not_found(request, exception):
    return render(request, '404.html', status=404)
