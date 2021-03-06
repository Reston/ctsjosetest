"""userctstest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from .userapp.urls import urlpatterns as user_urls

urlpatterns = [
    path('', include((user_urls, "user"), namespace='user')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.views.generic import TemplateView

    urlpatterns += [
        path('404/', TemplateView.as_view(template_name="404.html")),
    ]
