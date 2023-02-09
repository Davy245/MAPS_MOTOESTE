from django.urls import path
from .import views

urlpatterns = [
    path('route', views.route, name="route"),
    path('map', views.map, name="map"),
    path('', views.index, name="index"),
]