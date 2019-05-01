from django import forms 
from django.db import models
from django.contrib.auth.models import User

from .models import Review, Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['restaurant', 'score', 'title', 'review', 'photo']

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']