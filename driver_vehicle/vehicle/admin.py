from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'driver_id',
        'make',
        'model',
        'plate_number',
        'created_at',
        'updated_at'
    )
