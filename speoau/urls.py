from django.conf import settings
from django.conf.urls.static import static

from filebrowser.sites import site
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
   	
    url(r'^admin/', admin.site.urls),
    url(r'^members/', include('register.urls')),
    url(r'^posts/', include('posts.urls')),

	url(r'^$', views.home, name='home'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)