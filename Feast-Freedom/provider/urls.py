from django.contrib import admin
from django.urls import path, include,re_path
from .views import registerProviderView, registerKitchenView, listViewKitchen,my_image,viewKitchen


urlpatterns = [
    re_path(r'^register/',registerProviderView, name='register_provider'),
    re_path(r'^kitchen/',registerKitchenView , name='registerKitchenView'),
    path('', listViewKitchen.as_view(), name='kitchen-list'),
    re_path(r'(?P<pk>\d+)$', viewKitchen.as_view(), name='detail'),
]

