from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from my_app.forms import PostForm
from my_app.models import Post


class PostView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publish=True)
        return queryset


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('my_app:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy('my_app:list')

    def get_success_url(self):
        return reverse('my_app:view', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('my_app:list')
