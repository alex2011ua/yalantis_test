from django.test import TestCase, Client
from .models import Vehicle
from rest_framework import status
from django.urls import reverse
from .serializers import VehicleSerializer

client = Client()


class DriverTest(TestCase):
    def setUp(self):
        self.v_1 = Vehicle.objects.create(make='Alex', model='Alex', plate_number='AA 1234 FF')
        self.v_2 = Vehicle.objects.create(make='Alex2', model='Alex2', plate_number='AA 1235 FF')
        self.v_3 = Vehicle.objects.create(make='Alex3', model='Alex3', plate_number='AA 1236 FF')

    def test_get_all_driver(self):
        response = client.get(reverse('vehicle:get_list'))
        vehicle = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_driver(self):
        response = client.get(reverse('vehicle:vehicleRUD', kwargs={'pk': self.v_1.pk}))
        vehicle = Vehicle.objects.get(id=self.v_1.pk)
        serializer = VehicleSerializer(vehicle)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_driver(self):
        response = client.get(reverse('vehicle:vehicleRUD', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
