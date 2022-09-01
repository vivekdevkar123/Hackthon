
from django.shortcuts import render,redirect

from .models import Post,Category,Comment
from .forms import CommentForm
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
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.url)
    else:
        form = CommentForm()

    context = {
        'post' : post,
        'cats' : cats,
        'form': form
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
    return render(request,'category.html',{'cat':cat, 'posts':posts})

