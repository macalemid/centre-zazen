from django.http import HttpResponse
from django.shortcuts import render

context = {}

def home(request):
	return render(request, 'centre_zazen_sit/home.html')

def events(request):
	return render(request, 'centre_zazen_sit/events.html')

def restaurant(request):
	return render(request, 'centre_zazen_sit/restaurant.html')

def gallery(request):
	return render(request, 'centre_zazen_sit/gallery.html')

def feed(request):
	return render(request, 'centre_zazen_sit/feed.html')

def about(request):
	return render(request, 'centre_zazen_sit/about.html')

