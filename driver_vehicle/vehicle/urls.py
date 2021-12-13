from django.urls import path
from . import views


app_name = 'vehicle'
urlpatterns = [
    path('vehicle/', views.VehicleListCreateView.as_view()),
    path('vehicle/<int:pk>/', views.VehicleRUD.as_view()),
    path('set_driver/<int:pk>/', views.VehicleSetDriver.as_view()),

]
