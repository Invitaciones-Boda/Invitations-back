from django.urls import path
from . import views

urlpatterns = [
    path('ingreso/', views.ingreso, name='ingreso'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
