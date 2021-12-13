from rest_framework import generics
from vehicle.serializers import VehicleSerializer
from .models import Vehicle


class VehicleListCreateView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('with_drivers'):
            if request.GET.get('with_drivers') == 'yes':
                self.queryset = Vehicle.objects.filter(driver_id__isnull=False)
            else:
                self.queryset = Vehicle.objects.filter(driver_id__isnull=True)
        return self.list(request, *args, **kwargs)


class VehicleRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleSetDriver(generics.UpdateAPIView):

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
