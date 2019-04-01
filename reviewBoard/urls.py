"""pickmeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('', views.index, name="index"), #FBV #List
    # path('review/<int:pk>/', views.detail, name="review-detail"), #FBV #Detail
    path('', views.ReviewListView.as_view(), name="index"), #CBV #List
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name="review-detail"), #CBV #Detail
]
