from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Reply
from .forms import CreateForm, ReplyForm



def create_new(request):
    form = CreateForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('forum:cont_index')
    else:
        form = CreateForm()
    
    return render(request, 'forum/create.html', {'form': form})


def cont_index(request):
    posts = Thread.objects.all().order_by('-id')

    data ={
    'post_list': posts,   
    }

    return render(request, 'forum/cont_index.html', data)


def post_forum(request, id):
  post = Thread.objects.get(id=id)

  test = Thread.objects.all()
  thread = test.get(pk=id)
  formReply = ReplyForm(request.POST, None)
  replys = Reply.objects.all()
  

  if formReply.is_valid():
    post = formReply.save(commit=False)
    post.thread = thread
    post.save()
    return redirect('forum:post_forum', thread.id)
  else:
    formReply = ReplyForm()



  data ={
    'post': post,
    'thread': thread,
    'formReply': formReply,
    'replys': replys,
    'test': test
  }

  return render(request, 'forum/post_forum.html', data)

def comment_forum(request, id):
    test = Thread.objects.all()
    thread = test.get(pk=id)
    formReply = ReplyForm(request.POST, None)
    replys = Reply.objects.all()

    if formReply.is_valid():
        post = formReply.save(commit=False)
        post.thread = thread
        post.save()
        return redirect('forum:post_forum', thread.id)
    else:
        formReply = ReplyForm()
    
    context = {
        'thread': thread,
        'formReply': formReply,
        'replys': replys,
        'test': test
    }

    return render(request, 'forum/comment_forum.html', context)
