from django.contrib import admin
from .models import Category, Review, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'price_range', 'estimated_time', 'rating', 'is_featured')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'short_description', 'description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'rating', 'created_at')
    search_fields = ('name', 'comment', 'service__title')
