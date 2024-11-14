from django.db import models
from bagsApp.storage import OverwriteStorage
from bagsApp.fields import WEBPField
from ckeditor.fields import RichTextField


# Create your models here.

class newsModel(models.Model):
    def upload_location(instance, filename):
        return 'news/noticia_{}.webp'.format(instance.id)
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    image = WEBPField(default='newsdefault.webp', storage=OverwriteStorage ,upload_to=upload_location, blank=False)
    slug = models.SlugField(null=False, blank=False)
    
    def __str__(self):
        return self.title