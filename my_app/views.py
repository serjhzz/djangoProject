from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from my_app.models import Post


class PostView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('my_app:list')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('my_app:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('my_app:list')
