from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from my_app.forms import PostForm
from my_app.models import Post
from users.models import User


class PostHome(TemplateView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Post.objects.all()
        for obj in context_data['object_list']:
            author = Post.objects.get(id=obj.id).owner_id
            context_data['autor_name'] = User.objects.get(id=author).first_name
            print('author: ', User.objects.get(id=author).first_name)
        return context_data

    template_name = 'my_app/index.html'


class PostView(LoginRequiredMixin, ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_publish=True, owner=self.request.user)
        return queryset


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    permission_required = 'my_app.add_post'
    success_url = reverse_lazy('my_app:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    permission_required = 'my_app:change_post'

    # success_url = reverse_lazy('my_app:list')

    def get_success_url(self):
        return reverse('my_app:view', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = 'my_app:delete_post'
    success_url = reverse_lazy('my_app:list')
