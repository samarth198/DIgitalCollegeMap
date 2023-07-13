from django.contrib import admin
from django.urls import path,include
from map import views

urlpatterns = [
    path("",views.index,name = 'home'),
    path("map",views.map,name = 'map'),
    path("<int:class_num>",views.classroom,name = 'show-timetable'),
    path("add_lecture",views.add_lecture,name = 'add-lecture'),
    path("update_lecture/<lecture_id>",views.update_lect,name = 'update-lecture'),
    path("delete-lecture/<lecture_id>",views.delete_lect,name = 'delete-lecture'),
]