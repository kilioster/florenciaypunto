from django.shortcuts import render, get_object_or_404
from .models import BagsModel, BagsPhotos

def BagsView(request):
    bags = BagsModel.objects.all()
    return render(request, 'index.html', {'bags': bags})

def BagsSlug(request, slug):
    bag = BagsModel.objects.get(slug=slug)
    photoslist = BagsPhotos.objects.filter(bags=bag)
    return render(request, 'bagspost.html', {'bag': bag, 'photoslist': photoslist})

