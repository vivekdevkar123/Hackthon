
from cherrypy import url
from django.shortcuts import render

from .models import Post,Category
# Create your views here.

def home(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    context = {
        'posts':posts,
        'cats' : cats,
    }
    return render(request,'index.html',context)



def post(request, url):
    post = Post.objects.get(url = url)
    cats = Category.objects.all()
    context = {
        'post' : post,
        'cats' : cats,
    }
    return render(request, 'post.html',context)



def blogs(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'blogs.html',context)



def category(request,url):

    cat = Category.objects.get(url = url)
    posts = Post.objects.filter(cat=cat)

    context = {
        'cat':cat,
        'posts':posts,
    }
    return render(request,'category.html',context)

