from django.test import TestCase, Client
from .models import Driver
from rest_framework import status
from django.urls import reverse
from .serializers import DriverSerializer

client = Client()


class DriverTest(TestCase):
    def setUp(self):
        self.drive_1 = Driver.objects.create(first_name='Alex', last_name='Alex')
        self.drive_2 =Driver.objects.create(first_name='Alex1', last_name='Alex1')
        self.drive_3 =Driver.objects.create(first_name='Alex2', last_name='Alex2')

    def test_get_all_driver(self):
        response = client.get(reverse('driver:get_list'))
        driver = Driver.objects.all()
        serializer = DriverSerializer(driver, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_driver(self):
        response = client.get(reverse('driver:driverRUD'), args=1)
        driver = Driver.objects.get(pk=self.drive_1.pk)
        serializer = DriverSerializer(driver, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_invalid_driver(self):
    #     response = client.get(reverse('driver:driverRUD'), kwargs={'pk': 10})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
