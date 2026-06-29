from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('service', 'user', 'scheduled_date', 'scheduled_time', 'status', 'created_at')
    list_filter = ('status', 'service')
    search_fields = ('user__username', 'service__title', 'address', 'notes')
    date_hierarchy = 'scheduled_date'
