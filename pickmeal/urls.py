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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # 이게 없으면 login 페이지에 접근할 수 없다. 
    path('admin/', admin.site.urls),
    path('randfood/', include(('randFood.urls', 'randFood'), namespace='randFood')),
    path('', include(('reviewBoard.urls', 'reviewBoard'), namespace='reviewBoard')),
]

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),\
