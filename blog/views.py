from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.utils import timezone


def index(request):
    return HttpResponse('Hello World!')


def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'data': posts})
