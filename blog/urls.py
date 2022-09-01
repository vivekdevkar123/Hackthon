from django.urls import path,include
from .views import home,blogs,post,category

urlpatterns = [
    path('',home,name='home'),
    path('blogs/',blogs),
    path('blog/<slug:url>/', post),
    path('category/<slug:url>/',category),
]