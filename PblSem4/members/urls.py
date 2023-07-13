from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('profile',views.login_user,name = "profile"),
    path("logout_user",views.logout_user,name='logout'),
    path("register_user",views.register_user,name='register_user'),
]
#hello