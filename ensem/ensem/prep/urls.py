from django.urls import path, include
from .import views

app_name = 'prep'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
# urls.py
path('delete/<str:name>/', views.delete, name='delete'),
]
