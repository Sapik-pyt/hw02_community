from django.shortcuts import get_object_or_404, render
from yatube.settings import COUNT_LAST_POSTS
from .models import Group, Post


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:COUNT_LAST_POSTS]
    context = {
        'title': 'Записи сообщества',
        'text': 'Здесь будет информация о группах',
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context, slug)


def index(request):
    posts = Post.objects.all()[:COUNT_LAST_POSTS]
    context = {
        'title': 'Главная страница проекта Yatube',
        'text': 'Последнее обновление на сайте',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)
