from django.shortcuts import render
from bagsApp.models import BagsModel
from newsApp.models import newsModel

# Create your views here.
def IndexView(request):
    news = newsModel.objects.all().order_by('-id')[:3]
    bags = BagsModel.objects.all().order_by('-id')[:4]
    return render(request, 'index.html', {'bags': bags, 'news': news})