from django.urls import path
from .import views

app_name = 'settings'

urlpatterns = [
	path('index/', views.index, name='index'),
	path('config/', views.config, name='config'),
	path('time/', views.time, name='time'),
	path('building/', views.building, name='building'),
	path('room/', views.room, name='room'),
	]