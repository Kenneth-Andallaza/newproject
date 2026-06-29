import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicehub.settings')
django.setup()

from services.models import Service

mapping = {
    'AC Tune-Up & Maintenance': 'AC Tune-Up & Maintenance.jpg',
    'Deep Home Cleaning': 'Deep Home Cleaning.jpg',
    'Leak Detection & Repair': 'Leak Detection & Repair.jpg',
    'Outlet & Lighting Installation': 'Outlet & Lighting Installation.jpg',
    'Circuit Troubleshooting & Repair': 'Circuit Troubleshooting & Repair.jpg',
    'Drain Cleaning & Clog Removal': 'Drain Cleaning & Clog Removal.jpg',
    'Home Repair & Assembly': 'Home Repair & Assembly.jpg',
    'Interior Painting Touch-Up': 'Interior Painting Touch-Up.jpg',
    'Move-In / Move-Out Cleaning': 'MoveInMoveOutCleaning.jpg',
}

image_dir = PROJECT_ROOT / 'static' / 'images'
for title, filename in mapping.items():
    image_path = image_dir / filename
    if not image_path.exists():
        print(f'Missing file: {image_path}')
        continue
    service = Service.objects.filter(title=title).first()
    if not service:
        print(f'Service not found: {title}')
        continue

    if service.image and service.image.name:
        service.image.delete(save=False)

    with image_path.open('rb') as handle:
        service.image.save(image_path.name, File(handle), save=True)

    print(f'Assigned {filename} -> {service.title}')
