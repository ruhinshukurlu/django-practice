from django.shortcuts import render
from django.http import HttpResponse



def task_one(request):
    return HttpResponse("Walk in the streen for an hour!")


def task_two(request):
    return HttpResponse("Do another thing!")