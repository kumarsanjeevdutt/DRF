from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    students=[
        {
            'name':"Sanjeev",
            'Age':25,
            "course":"EC"
        }
        ]
    return HttpResponse(students)