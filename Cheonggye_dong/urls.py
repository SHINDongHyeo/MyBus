from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('busstation', views.busstation, name='busstation'),
]