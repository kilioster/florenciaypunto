from django.shortcuts import render
from .models import newsModel

# Create your views here.
def NewsView(request):
    news = newsModel.objects.all()
    return render(request, 'index.html', {'news': news})

def NewsSlug(request, slug):
    new = newsModel.objects.get(slug=slug)
    return render(request, 'newspost.html', {'new': new})

def NewsHistory(request):
    newshist = newsModel.objects.all().order_by('-id')
    return render(request, 'newshist.html', {'newshist': newshist})