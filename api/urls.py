from django.urls import path
from . import views

urlpatterns = [
    path('client', views.getClients),
    path('client/add', views.addClient),
]