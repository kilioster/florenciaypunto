from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'news'

urlpatterns = [
    path('', views.NewsView, name='list_news'),
    path('<slug:slug>', views.NewsSlug, name="page"),
    path('newshist/', views.NewsHistory, name="newshistory")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)