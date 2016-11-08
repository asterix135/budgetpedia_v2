from django.shortcuts import render
from chartit import Chart, DataPool

# Create your views here.

def index(request):
    return render(request, 'explorer/index.html')


def process(request):
    return render(request, 'explorer/process.html')


def impact(request):
    return render(request, 'explorer/impact.html')


def detail(request):
    # play with chartit to figure out how to serve pie chart
    return render(request, 'explorer/detail.html')
