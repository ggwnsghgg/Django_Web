from blog.apps import BlogConfig
from django.http import request
from django.shortcuts import redirect, render
from blog.models import Category, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone 
from .form import BlogUpdate
from .models import Post

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }

    return render(req, "index.html", context=context)

def list_index(req):
    post_latests = Post.objects.order_by("-createDate")[:20]
    context = {
        "post_latest": post_latests
    }

    return render(req, "post_list.html", context=context)

def delete(request, post_id):
    post_latest = Post.objects.get(id=post_id)
    post_latest.delete()
    return redirect('/')



def edit(request,post_id):
    blog = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = BlogUpdate(request.POST, request.FILES)
        if form.is_valid(): 
            print(form.cleaned_data)
            blog.title = form.cleaned_data['title']
            blog.title_image = form.cleaned_data['title_image']
            blog.title_image2 = form.cleaned_data['title_image2']
            blog.title_image3 = form.cleaned_data['title_image3']
            # blog.category = form.cleaned_data['category']
            blog.content = form.cleaned_data['content']
            blog.save()
            blog.put_date = timezone.datetime.now()
            messages.success(request, "수정되었습니다.")
            return redirect('/')

    else:
        form = BlogUpdate(instance = blog)
        return render(request, 'blog/post_edit.html/', {'form':form})
        
class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "title_image","title_image2","title_image3","content", "category"]


