from django.shortcuts import render
from django.http import HttpResponse
def home(request):
   # return HttpResponse(request,'123.html')
    return render (request,'adventure 3.3.html')
