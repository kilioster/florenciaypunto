from django.contrib import admin
from .models import newsModel

# Register your models here.
class newsADM(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author')

admin.site.register(newsModel, newsADM)