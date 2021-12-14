from django.urls import path
from . import views


app_name = 'vehicle'
urlpatterns = [
    path('vehicle/', views.VehicleListCreateView.as_view(), name='get_list'),
    path('vehicle/<int:pk>/', views.VehicleRUD.as_view(), name='vehicleRUD'),
    path('set_driver/<int:pk>/', views.VehicleSetDriver.as_view()),

]
