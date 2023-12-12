from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('me/', views.me, name='me'),
    path('home_result/', views.home, name='home_result')
]
