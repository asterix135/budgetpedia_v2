from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'explorer/index.html')


def process(request):
    return render(request, 'explorer/process.html')


def impact(request):
    return render(request, 'explorer/impact.html')


def detail(request):
    return render(request, 'explorer/detail.html')
