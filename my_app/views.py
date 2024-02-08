from django.shortcuts import render

from my_app.models import Post


def index(request):
    context = {
        'object_list': Post.objects.all(),
        'title': 'Посты'
    }
    return render(request, 'blog/index.html', context)
