# ServiceHub

ServiceHub is a modern home services booking platform built with Django, Bootstrap 5, and SQLite.

## Features
- User authentication and profile management
- Service listings and detail pages
- Booking system with booking history and cancellation
- Contact form and blog section
- Custom admin dashboard for staff
- Responsive premium UI with animations

## Setup

1. Activate the virtual environment:
   ```powershell
   cd c:\xampp\htdocs\newproject
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
3. Run database migrations:
   ```powershell
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```powershell
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```powershell
   python manage.py runserver
   ```

## Notes
- Media uploads are configured under `media/`.
- Static assets are served from `static/` in development.
- Add staff users to access the admin dashboard at `/dashboard/`.
