from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('test_login', views.carga_login, name='carga_login'),
]