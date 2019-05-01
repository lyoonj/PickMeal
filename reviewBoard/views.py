# View, Render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Login Required Decorator
from django.utils.decorators import method_decorator
from django.contrib.auth import views, models, login, decorators 
from django.contrib.auth.decorators import login_required 

# model, form
from .models import Restaurant, Review
from .forms import UserForm, ReviewForm, RestaurantForm


#################### Mixins ####################
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView

# code source : https://gist.github.com/michelts/1029336
class MultipleFormsMixin(FormMixin):
    """
    A mixin that provides a way to show and handle several forms in a
    request.
    """
    form_classes = {} # set the form classes as a mapping

    def get_form_classes(self):
        return self.form_classes

    def get_forms(self, form_classes):
        return dict([(key, klass(**self.get_form_kwargs())) \
            for key, klass in form_classes.items()])

    def forms_valid(self, forms):
        return super(MultipleFormsMixin, self).form_valid(forms)

    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))


class ProcessMultipleFormsView(ProcessFormView):
    """
    A mixin that processes multiple forms on POST. Every form must be
    valid.
    """
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))

    def post(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)

        # form의 'name' 값에 따라서 제출되는 폼이 달라진다.
        if 'ReviewForm' in request.POST:
            form_class = self.form_classes['ReviewForm']
            form_name = 'ReviewForm'
        else:
            form_class = self.form_classes['RestaurantForm']
            form_name = 'RestaurantForm'

        # 둘 중 제출된 폼에 따라 form 변수에 저장
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else: 
            return self.render_to_response(self.get_context_data(forms=forms))


class BaseMultipleFormsView(MultipleFormsMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """

class MultipleFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaing several forms, and rendering a template response.
    """


#################### Class Based View ####################
# List
class ReviewListView(ListView) :
    model = Restaurant
    template_name = "reviewBoard/index.html"
    context_object_name = "restaurants"

# Detail
class ReviewDetailView(DetailView):
    model = Review # 해당 모델 - URLConf 의 PK 변수를 활용하여 해당 모델의 특정 record를 컨텍스트 변수(object)에 담는다.
    template_name = 'reviewBoard/review_detail.html' # 디폴트 템플릿명: <app_label>/<model_name>_detail.html
    context_object_name = 'review' 

# New Review
class ReviewCreateView(CreateView, MultipleFormsView):
    model = Review
    fields = ('writer','restaurant', 'score', 'title', 'review', 'photo')
    template_name = 'reviewBoard/review_new.html'
    success_url = '/'
    form_classes = {'ReviewForm': ReviewForm,
                    'RestaurantForm': RestaurantForm}

    # 로그인 요구
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReviewCreateView, self).dispatch(*args, **kwargs)

    def get_review_initial(self):
        return {'title':'title test',
                'restaurant': '신탕떡볶이',
                'score': 3.0,
                'review':'test',
                }

    def get_restaurant_initial(self):
        return {'name':'restaurant name',
                'location': 'somewhere',
                'category':'한식'}

class ReviewUpdateView(UpdateView):
    model = Review
    context_object_name = 'review'
    form_class = ReviewForm
    template_name = 'reviewBoard/review_update.html'
    success_url = '/'

    #get object
    def get_object(self): 
        review = get_object_or_404(Review, pk=self.kwargs['pk'])

        return review

# New User
class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'reviewBoard/signup.html'
    success_url = "/"



