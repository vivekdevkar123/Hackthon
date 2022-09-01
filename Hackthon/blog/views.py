from django.shortcuts import render
from matplotlib.style import context

# Create your views here.

def home(request):
    context = {

    }
    return render(request,'index.html',context)

def post(request):
    context = {

    }
    return render(request,'post.html',context)

def bloglist(request):
    context = {

    }
    return render(request,'bloglist.html',context)

