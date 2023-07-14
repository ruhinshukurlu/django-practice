from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



# def task_one(request):
#     return HttpResponse("Walk in the streen for an hour!")


# def task_two(request):
#     return HttpResponse("Do another thing!")


def get_monthly_task(request, month):
    task_text = None

    if month == "january":
        task_text = "Walk in the streen for an hour!"
    elif month == "february":
        task_text = "Do another thing!"
    else:
        return HttpResponseNotFound("This month isn't supported")

    return HttpResponse(task_text)
