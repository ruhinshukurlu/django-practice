from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="tasks-list"),
    path("<int:month>", views.get_monthly_task_bynumber),
    path("<str:month>", views.get_monthly_task, name="monthly-task"),
]