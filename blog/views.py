from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.template.defaultfilters import slugify
from .forms import PostModelForm

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    queryset = Post.objects.all()
    template_name = 'blog/create_post.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(self.request.POST.get("title"))
        obj.save()
        return HttpResponseRedirect('/blog/')