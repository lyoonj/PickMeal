from rest_framework import serializers
from .models import Restaurant, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Restaurant
        fields = ('name',
                  'location',
                  'category',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Review
        fields = ('restaurant', 
                  'score', 
                  'title',
                  'review',)


