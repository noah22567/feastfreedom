"""mainset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include,re_path
from django.views.generic.base import TemplateView
from provider.views import registerProviderView, registerKitchenView
from users.views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/users/', include('users.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/profile/', TemplateView.as_view(template_name='home.html'), name='home'),
    re_path(r'^provider/register',registerProviderView, name='register_provider'),
    re_path(r'^provider/kitchen',registerKitchenView , name='register_provider'),

    # path('admin/users/myuser/add/', TemplateView.as_view(template_name='home.html'))
    re_path(r'signup/$', signup, name='signup'),
]
