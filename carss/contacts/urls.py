from django.urls import path

from . import views

urlpatterns = [
    # path() - arg1: route, arg2: linked views method, agr3(optional): url name
    path('contact', views.contact, name='contact'),
]
