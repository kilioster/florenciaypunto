from django.db import models
from multiselectfield import MultiSelectField
from .storage import OverwriteStorage
from .fields import WEBPField
import uuid

# Create your models here.
class BagsModel(models.Model):
    def upload_location(instance, filename):
        return 'bags/bag_{}.webp'.format(instance.id)
    
    MY_MATERIALS = (
        ('Algodon', 'Algodon'),
        ('Hilo', 'Hilo'),
        ('Trapillo', 'Trapillo'),
        ('Lana', 'Lana'),
    )
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=700)
    material= MultiSelectField(choices=MY_MATERIALS, max_choices=3, max_length=50, blank=False, null=False)
    price = models.IntegerField()
    image = WEBPField(default='newsdefault.webp', storage=OverwriteStorage ,upload_to=upload_location, blank=False)
    slug = models.SlugField(default='', null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class BagsPhotos(models.Model):
    def upload_location(instance, filename):
        unique_id = uuid.uuid4()
        return 'bags/{}/{}.webp'.format(instance.bags.slug, unique_id)
    
    bags = models.ForeignKey(BagsModel, default=None, on_delete=models.CASCADE)
    images = WEBPField(upload_to=upload_location)
    
    def __str__(self):
        return self.bags.name