from django.shortcuts import get_object_or_404, render
from .models import Category, Service

SERVICE_IMAGE_MAP = {
    'leak-detection-repair': 'Leak Detection & Repair.jpg',
    'drain-cleaning-clog-removal': 'Drain Cleaning & Clog Removal.jpg',
    'outlet-lighting-installation': 'Outlet & Lighting Installation.jpg',
    'circuit-troubleshooting-repair': 'Circuit Troubleshooting & Repair.jpg',
    'deep-home-cleaning': 'Deep Home Cleaning.jpg',
    'move-in-move-out-cleaning': 'MoveInMoveOutCleaning.jpg',
    'ac-tune-up-maintenance': 'AC Tune-Up & Maintenance.jpg',
    'heating-system-inspection': 'Heating System Inspection.jpg',
    'home-repair-assembly': 'Home Repair & Assembly.jpg',
    'interior-painting-touch-up': 'Interior Painting Touch-Up.jpg',
}


def _assign_static_image(service, default='service-card.jpg'):
    service.static_image = SERVICE_IMAGE_MAP.get(service.slug, default)
    return service


def service_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    services = Service.objects.select_related('category').all()
    categories = Category.objects.all()

    if query:
        services = services.filter(title__icontains=query) | services.filter(short_description__icontains=query)
    if category_slug:
        services = services.filter(category__slug=category_slug)

    featured = services.filter(is_featured=True)[:4]
    services = [ _assign_static_image(service) for service in services ]
    featured = [ _assign_static_image(service) for service in featured ]
    return render(request, 'services/service_list.html', {
        'services': services,
        'categories': categories,
        'featured': featured,
        'query': query,
        'selected_category': category_slug,
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.filter(category=service.category).exclude(id=service.id)[:4]
    _assign_static_image(service, default='service-detail.svg')
    related_services = [ _assign_static_image(related) for related in related_services ]
    return render(request, 'services/service_detail.html', {
        'service': service,
        'related_services': related_services,
    })
