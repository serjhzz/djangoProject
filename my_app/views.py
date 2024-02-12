from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from my_app.models import Post


class PostView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publish=True)
        return queryset


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('my_app:list')


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview']
    # success_url = reverse_lazy('my_app:list')

    def get_success_url(self):
        return reverse('my_app:list', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('my_app:list')
