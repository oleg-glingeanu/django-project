from django.http import HttpResponse
from django.shortcuts import render

def news(request):
    return render(request,'news_page.html')

def covid(request):
    return render(request,'covid_page.html')

def events(request):
    return render(request,'events_page.html')