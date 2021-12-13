from django.contrib import admin
from driver.models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'created_at',
        'updated_at'
    )
