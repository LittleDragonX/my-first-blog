from django.shortcuts import render, HttpResponse
from blog.models import Post


def index(request):
    return HttpResponse('Hello World!')


def post_list(request):
    data = Post.objects.all()
    return render(request, 'blog/post_list.html', {'data': data})
