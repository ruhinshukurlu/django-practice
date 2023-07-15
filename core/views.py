from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_tasks = {
    "january":"Walk in the streen for an hour!",
    "february":"Feb tasks",
    "march":"March tasks",
    "april":"april tasks",
    "may":"may tasks",
    "june":"june tasks",
    "july":"july tasks",
    "august":"august tasks",
    "september":"september tasks",
    "october":"october tasks",
    "november":"november tasks",
    "december":"december tasks",
}


def index(request):
    months = list(monthly_tasks.keys())
    list_items = ""

    for month in months:
        capitalized_month = month.capitalize()
        path = reverse("monthly-task", args=[month])
        list_items += f"<li><a href='{path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def get_monthly_task_bynumber(request, month):
    months = list(monthly_tasks.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    redirect_path = reverse("monthly-task", args=[redirect_month])
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)


def get_monthly_task(request, month):
    try:
        task_text = monthly_tasks[month]
        response_data = render_to_string("tasks/task.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Not found such a month!")

