from rest_framework import generics
from driver.serializers import DriverSerializer
from .models import Driver

import datetime


class DriverListCreateView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('created_at__gte'):
            date = datetime.datetime.strptime(request.GET.get('created_at__gte'), "%d-%m-%Y")
            self.queryset = Driver.objects.filter(created_at__gte=date)
        elif request.GET.get('created_at__lte'):
            date = datetime.datetime.strptime(request.GET.get('created_at__lte'), "%d-%m-%Y")
            self.queryset = Driver.objects.filter(created_at__lte=date)
        return self.list(request, *args, **kwargs)


class DriverRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
