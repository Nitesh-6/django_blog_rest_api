from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def blog_list(req):
    data = {
        "message": "Hello World!"
    }
    return JsonResponse(data=data)