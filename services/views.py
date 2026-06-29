from django.shortcuts import get_object_or_404, render
from .models import Category, Service


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
    return render(request, 'services/service_detail.html', {
        'service': service,
        'related_services': related_services,
    })
