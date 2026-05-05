from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_registros, name='lista_registros'),
]