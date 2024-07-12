from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name ='home'),
    path("toDos/", views.toDo, name = 'toDo')
]









