from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
class Postview(ListView):
	model = Post
	template_name = "post.html"
	ordering = ['-id']

class  Detailview(DetailView):
	model = Post
	template_name ="article-detail.html"

class AddPost(CreateView):
	model = Post
	form_class = PostForm
	template_name = "blog_post.html"
	#fields = '__all__'
class UpdatePost(UpdateView):
	model = Post
	template_name = "update.html"
	fields = ["title","body"]
class DeletePost(DeleteView):
	model = Post
	template_name = "delete_post.html"
	success_url = reverse_lazy("post")