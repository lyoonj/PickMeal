from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse 
from django.views.generic import ListView, DetailView
from django.http import HttpResponse 
from django.contrib.auth import views
from .models import Restaurant, Review

# HttpResponse
# def index(request) :
#     return HttpResponse("One More Scoop")

# def detail(request, pk) :
#     review = get_object_or_404(Review, pk=pk) 

#     return render(request, "reviewBoard/review_detail.html", {'review' : review})

class ReviewListView(ListView) :
    """
	ListView 디폴트 지정 속성 : 컨텍스트를 쓸 때, model만 쓸 때 
	1) 컨텍스트 변수 : object_list (default 이름)
	2) 템플릿 파일 : readinglist_list.html (모델명 소문자_list.html)
	"""
    model = Restaurant
    template_name = "reviewBoard/index.html"
    context_object_name = "restaurants"


#디테일 뷰 만들기
class ReviewDetailView(DetailView):
    model = Review # 해당 모델 - URLConf 의 PK 변수를 활용하여 해당 모델의 특정 record를 컨텍스트 변수(object)에 담는다.
    template_name = 'reviewBoard/review_detail.html' # 디폴트 템플릿명: <app_label>/<model_name>_detail.html
    context_object_name = 'review' 
