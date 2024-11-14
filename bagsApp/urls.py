from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bags'

urlpatterns = [
    path('', views.BagsView, name='list_bag'),
    path('<slug:slug>', views.BagsSlug, name="page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)