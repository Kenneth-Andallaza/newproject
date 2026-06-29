from django.db import migrations


def create_initial_services(apps, schema_editor):
    Category = apps.get_model('services', 'Category')
    Service = apps.get_model('services', 'Service')

    categories = [
        {
            'name': 'Plumbing',
            'slug': 'plumbing',
            'description': 'Fast, licensed plumbing repairs for leaks, pipes, drains, and bathroom fixtures.',
            'icon': 'droplet',
        },
        {
            'name': 'Electrical',
            'slug': 'electrical',
            'description': 'Qualified electricians for wiring, outlets, lighting, and safety inspections.',
            'icon': 'lightning-charge',
        },
        {
            'name': 'Cleaning',
            'slug': 'cleaning',
            'description': 'Home cleaning services from one-time deep cleans to weekly upkeep and move-outs.',
            'icon': 'broom',
        },
        {
            'name': 'HVAC',
            'slug': 'hvac',
            'description': 'Air conditioning and heating service, maintenance, and urgent repairs.',
            'icon': 'snow',
        },
        {
            'name': 'Handyman',
            'slug': 'handyman',
            'description': 'General home repairs, furniture assembly, mounting, and small renovation tasks.',
            'icon': 'tools',
        },
    ]

    category_objects = {}
    for category_data in categories:
        category, _ = Category.objects.get_or_create(
            slug=category_data['slug'],
            defaults={
                'name': category_data['name'],
                'description': category_data['description'],
                'icon': category_data['icon'],
            },
        )
        category_objects[category.slug] = category

    services = [
        {
            'category': category_objects['plumbing'],
            'title': 'Leak Detection & Repair',
            'slug': 'leak-detection-repair',
            'short_description': 'Find and fix pipe leaks, dripping faucets, and hidden water damage fast.',
            'description': 'Certified plumbers diagnose leaks, replace worn valves, repair burst pipes, and restore proper water flow with minimal disruption.',
            'price_range': '$80 - $220',
            'estimated_time': '1-3 hours',
            'rating': 4.9,
            'is_featured': True,
        },
        {
            'category': category_objects['plumbing'],
            'title': 'Drain Cleaning & Clog Removal',
            'slug': 'drain-cleaning-clog-removal',
            'short_description': 'Clear kitchen, bathroom, and main line clogs with professional drain service.',
            'description': 'Technicians use safe hydro-jetting and root removal tools to clear blockages and prevent future backups.',
            'price_range': '$75 - $180',
            'estimated_time': '1-2 hours',
            'rating': 4.8,
            'is_featured': False,
        },
        {
            'category': category_objects['electrical'],
            'title': 'Outlet & Lighting Installation',
            'slug': 'outlet-lighting-installation',
            'short_description': 'Install new outlets, switches, ceiling fixtures, and energy-efficient lighting.',
            'description': 'Licensed electricians handle wiring, switch upgrades, dimmer installs, and indoor/outdoor lighting safely and neatly.',
            'price_range': '$90 - $260',
            'estimated_time': '1-4 hours',
            'rating': 4.8,
            'is_featured': True,
        },
        {
            'category': category_objects['electrical'],
            'title': 'Circuit Troubleshooting & Repair',
            'slug': 'circuit-troubleshooting-repair',
            'short_description': 'Diagnose breakers, tripping circuits, and intermittent power issues quickly.',
            'description': 'Experts inspect panels, replace faulty breakers, and repair wiring faults to restore stable power.',
            'price_range': '$110 - $320',
            'estimated_time': '2-5 hours',
            'rating': 4.7,
            'is_featured': False,
        },
        {
            'category': category_objects['cleaning'],
            'title': 'Deep Home Cleaning',
            'slug': 'deep-home-cleaning',
            'short_description': 'Comprehensive deep cleaning for kitchens, bathrooms, living areas, and bedrooms.',
            'description': 'Our cleaning crew removes grime, sanitizes surfaces, and refreshes every room for a healthy home environment.',
            'price_range': '$120 - $280',
            'estimated_time': '3-6 hours',
            'rating': 4.9,
            'is_featured': True,
        },
        {
            'category': category_objects['cleaning'],
            'title': 'Move-In / Move-Out Cleaning',
            'slug': 'move-in-move-out-cleaning',
            'short_description': 'Prepare your home for moving with a professional clean from top to bottom.',
            'description': 'This service includes floor care, appliance cleaning, bathroom scrubbing, and dust removal to get the space move-in ready.',
            'price_range': '$150 - $350',
            'estimated_time': '4-7 hours',
            'rating': 4.8,
            'is_featured': False,
        },
        {
            'category': category_objects['hvac'],
            'title': 'AC Tune-Up & Maintenance',
            'slug': 'ac-tune-up-maintenance',
            'short_description': 'Seasonal AC maintenance to improve efficiency and prevent breakdowns.',
            'description': 'HVAC professionals clean filters, check refrigerant levels, test thermostats, and optimize cooling performance for reliable comfort.',
            'price_range': '$95 - $180',
            'estimated_time': '1-2 hours',
            'rating': 4.9,
            'is_featured': True,
        },
        {
            'category': category_objects['hvac'],
            'title': 'Heating System Inspection',
            'slug': 'heating-system-inspection',
            'short_description': 'Safety check and tune-up for furnaces, heat pumps, and ductwork.',
            'description': 'Technicians inspect heating systems, replace filters, and ensure efficient operation before winter arrives.',
            'price_range': '$90 - $200',
            'estimated_time': '1-2 hours',
            'rating': 4.8,
            'is_featured': False,
        },
        {
            'category': category_objects['handyman'],
            'title': 'Home Repair & Assembly',
            'slug': 'home-repair-assembly',
            'short_description': 'Small repairs, shelving, furniture assembly, mounting, and general home fixes.',
            'description': 'Trusted handymen complete to-do list tasks, install shelves, repair doors, and handle common home repair jobs.',
            'price_range': '$70 - $240',
            'estimated_time': '1-4 hours',
            'rating': 4.8,
            'is_featured': False,
        },
        {
            'category': category_objects['handyman'],
            'title': 'Interior Painting Touch-Up',
            'slug': 'interior-painting-touch-up',
            'short_description': 'Refresh one room with wall patching and expert paint touch-ups.',
            'description': 'Experienced painters fix nail holes, patch imperfections, and apply a smooth new coat to brighten interiors.',
            'price_range': '$130 - $320',
            'estimated_time': '2-5 hours',
            'rating': 4.7,
            'is_featured': False,
        },
    ]

    for service_data in services:
        Service.objects.get_or_create(
            slug=service_data['slug'],
            defaults=service_data,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_services),
    ]
