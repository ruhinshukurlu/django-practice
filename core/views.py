from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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

def get_monthly_task_bynumber(request, month):
    months = list(monthly_tasks.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month]
    return HttpResponseRedirect("/tasks/" + redirect_month)


def get_monthly_task(request, month):
    try:
        task_text = monthly_tasks[month]
        return HttpResponse(task_text)
    except:
        return HttpResponseNotFound("Not found such a month!")

