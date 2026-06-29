from django.contrib import admin
from .models import CustomerProfile, Notification


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'state', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone', 'city', 'state')
    list_filter = ('city', 'state')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_read', 'created_at')
    search_fields = ('user__username', 'title', 'message')
    list_filter = ('is_read',)
