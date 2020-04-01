from django.urls import path

from . import views

urlpatterns = [
    # path() - arg1: route, arg2: linked views method, agr3(optional): url name
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]
