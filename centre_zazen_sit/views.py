from django.http import HttpResponse
from django.shortcuts import render

context = {}

def index(request):
	return render(request, 'centre_zazen_sit/home.html')