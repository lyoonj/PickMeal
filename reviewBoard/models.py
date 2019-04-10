import PIL
from django.db import models
from .validators import validate_score
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model) :
    cat_food = (
        ("한식","한식"),
        ("중식","중식"),
        ("일식","일식"),
        ("양식","양식"),
    )

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=cat_food) 

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name 

class Review(models.Model) :
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)

    writer = models.CharField(max_length=200, default=None, null=True)
    created_by = models.ForeignKey(User, 
                                    default=None, null=True,
                                    on_delete=models.CASCADE)

    score = models.FloatField(default=None, null=True, validators=[validate_score])
    title = models.CharField(max_length=50)
    review = models.TextField()
    photo = models.ImageField(upload_to="reviewBoard/images", blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
