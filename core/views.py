from django.shortcuts import render
from .models import  Post
from django.core.paginator import Paginator


def index(request):
  posts = Post.objects.all().order_by('-id')

  paginator = Paginator(posts,2)
  page_num = request.GET.get('page')
  page = paginator.get_page(page_num)

  data ={
    'post_list': posts,
    'page': page,
  }
  return render(request, 'core/index.html', data)

def post(request, id):
  post = Post.objects.get(id=id)
  data ={
    'post': post,
  }
  return render(request, 'core/post.html', data)
