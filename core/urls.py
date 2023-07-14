from django.urls import path
from . import views

urlpatterns = [
    path("task1", views.task_one),
    path("task2", views.task_two)
]