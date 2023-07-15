from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_tasks = {
    "january":"Walk in the streen for an hour!",
    "february":"Feb tasks detail",
    "march":"March tasks detail",
    "april":"april tasks detail",
    "may":"may tasks detail",
    "june":"june tasks detail",
    "july":"july tasks detail",
    "august":"august tasks detail",
    "september":"september tasks detail",
    "october":"october tasks detail",
    "november":"november tasks detail",
    "december":"december tasks detail",
}


def index(request):
    months = list(monthly_tasks.keys())
    return render(request, "tasks/index.html", {"months":months})


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
        return render(request, "tasks/task.html", { "task":task_text, "month":month })
    except:
        return HttpResponseNotFound("Not found such a month!")

