from django.shortcuts import render
from  django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = "post_delete.html"
    template_name = "base.html"
  
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "post_form.html"
    
  
class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "post_confirm_delete.html"
    