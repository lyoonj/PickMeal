from django.shortcuts import render
from django.db.models import Max, Avg
from reviewBoard.models import Review, Restaurant
import random

# Create your views here.
def get_random_restaurant():
    max_id = Restaurant.objects.all().aggregate(max_id = Max("id"))['max_id']
    while True : 
        pk = random.randint(1, max_id)
        restaurant = Restaurant.objects.filter(pk=pk).first()
        if restaurant : 
            return restaurant

def index(request):
    restaurant = get_random_restaurant()
    score_avg = Review.objects.filter(restaurant__name=restaurant.name).aggregate(Avg('score'))

    return render(request, 'randFood/index.html', {'restaurant':restaurant, 'score_avg':score_avg})
