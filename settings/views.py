from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def config(request):
	return render(request, 'config.html')

def time(request):
	return render(request, 'time.html')

def building(request):
	return render(request, 'building.html')

def room(request):
	return render(request, 'room.html')