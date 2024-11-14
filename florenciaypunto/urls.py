from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from bagsApp import views as viewsbags
from newsApp import views as viewsnews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name='index'),
    path('bags/', include('bagsApp.urls')),
    path('news/', include('newsApp.urls')),
    path('newshist/', viewsnews.NewsHistory, name="newshistory")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
