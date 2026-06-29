from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

base = Path(__file__).resolve().parent.parent / 'static' / 'images'
base.mkdir(parents=True, exist_ok=True)

jpg_specs = [
    ('service-card.jpg', (1000, 700), (45, 125, 210), 'Service Card'),
    ('blog-card.jpg', (1000, 700), (30, 180, 110), 'Blog Card'),
]

for name, size, color, label in jpg_specs:
    path = base / name
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype('arial.ttf', 64)
    except Exception:
        font = ImageFont.load_default()
    bbox = font.getbbox(label)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.rectangle([((size[0]-w)//2-20, (size[1]-h)//2-20), ((size[0]+w)//2+20, (size[1]+h)//2+20)], fill=(255,255,255,180))
    draw.text(((size[0]-w)//2, (size[1]-h)//2), label, font=font, fill=(10, 10, 10))
    img.save(path, quality=90)

svg_templates = {
    'plumbing.svg': ('#4b8bf5', 'Plumbing'),
    'electrical.svg': ('#f5c542', 'Electrical'),
    'cleaning.svg': ('#42c4a6', 'Cleaning'),
    'hvac.svg': ('#4fb0f5', 'HVAC'),
    'handyman.svg': ('#f57b42', 'Handyman'),
}

for name, (bg, label) in svg_templates.items():
    path = base / name
    svg = f'''<svg width="1200" height="800" viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="800" rx="48" fill="{bg}" />
  <circle cx="600" cy="320" r="160" fill="#ffffff" fill-opacity="0.18" />
  <text x="600" y="450" text-anchor="middle" font-family="Arial, sans-serif" font-size="80" fill="#ffffff" font-weight="700">{label}</text>
  <text x="600" y="540" text-anchor="middle" font-family="Arial, sans-serif" font-size="36" fill="#ffffff" opacity="0.85">ServiceHub Sample</text>
</svg>'''
    path.write_text(svg, encoding='utf-8')

print('Created sample images in', base)
