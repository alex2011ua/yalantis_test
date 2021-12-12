from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from .models import Vehicle
from .serializers import VehicleSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def delete(self, request, pk=None):
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.delete()
        return Response(data(self.serializer_class(vehicle)), 204)

