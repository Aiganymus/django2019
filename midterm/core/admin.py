from django.contrib import admin

# Register your models here.
from django.contrib import admin
from core.models import Product, Service


@admin.register(Product)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'size',)


@admin.register(Service)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_type', 'approximate_duration',)