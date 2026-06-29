from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from services.models import Service
from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request, slug):
    service = get_object_or_404(Service, slug=slug)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.save()
            messages.success(request, 'Your booking request has been submitted successfully.')
            return redirect('booking-history')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {
        'service': service,
        'form': form,
    })


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user).select_related('service').order_by('-created_at')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status not in ['completed', 'cancelled']:
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.warning(request, 'This booking cannot be cancelled.')
    return redirect('booking-history')
