from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse 
from django.views.generic import ListView, DetailView
from django.http import HttpResponse 
from django.contrib.auth import views
from .models import Restaurant, Review

# HttpResponse
# def index(request) :
#     return HttpResponse("One More Scoop")

def index(request) :
    restaurants = Restaurant.objects.all()
    # restaurants = Review.objects.select_related('restaurant')
    
    return render(request, "reviewBoard/index.html", {'restaurants' : restaurants})


