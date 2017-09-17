from django.shortcuts import render
#from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post

from rest_framework import viewsets
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer


def post_list(request):
    posts = Post.objects.published()
    #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    does_like = post.likes.filter().exists()
    if does_like: #TODO check if user is authenticated
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    return HttpResponse('ok')


