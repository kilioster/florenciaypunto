from django.contrib import admin
from .models import BagsModel, BagsPhotos

# Register your models here.
class BagsImageAdmin(admin.StackedInline):
    model = BagsPhotos
    
@admin.register(BagsModel)
class BagsAdmin(admin.ModelAdmin):
    inlines = [BagsImageAdmin]
    list_display = ['name', 'material', 'price']
    
    class meta:
        model = BagsModel

@admin.register(BagsPhotos)
class BagImageAdmin(admin.ModelAdmin):
    pass