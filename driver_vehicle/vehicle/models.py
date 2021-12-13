from django.db import models
from driver.models import Driver


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=10)  # todo  format example "AA 1234 OO"
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
