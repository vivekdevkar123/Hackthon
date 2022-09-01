from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
