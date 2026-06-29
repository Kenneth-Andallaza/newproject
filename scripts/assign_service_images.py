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

base_dir = Path(__file__).resolve().parent.parent
image_dir = base_dir / 'static' / 'images'
image_files = [
    path for path in image_dir.iterdir()
    if path.is_file() and path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp', '.svg'}
]

for service in Service.objects.all():
    if service.image:
        print(f'Skipped {service.title}: already has an image')
        continue

    keywords = [
        service.category.name.lower(),
        service.category.slug.lower(),
        service.slug.lower(),
        service.title.lower().replace('&', '').replace('/', '').replace('-', ' '),
    ]

    matched_path = None
    for path in image_files:
        name = path.stem.lower()
        if any(keyword in name for keyword in keywords):
            matched_path = path
            break

    if matched_path is None:
        print(f'No matching image found for {service.title}')
        continue

    with matched_path.open('rb') as handle:
        service.image.save(matched_path.name, File(handle), save=True)

    print(f'Assigned {matched_path.name} -> {service.title}')
