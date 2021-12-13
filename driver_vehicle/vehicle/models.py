from django.db import models
from driver.models import Driver
from django.core.validators import RegexValidator


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=10, validators=[RegexValidator(r'\w\w \d\d\d\d \w\w')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
