from django.http import HttpResponse
from django.shortcuts import render

def events(request):
    return render(request,'events_page.html')