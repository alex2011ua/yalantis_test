from django.urls import path
from . import views


app_name = 'driver'
urlpatterns = [
    path('driver/', views.DriverListCreateView.as_view()),
    path('driver/<int:pk>/', views.DriverRUD.as_view()),

]