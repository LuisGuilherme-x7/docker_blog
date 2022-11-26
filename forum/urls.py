from django.urls import path
from .views import create_new, cont_index, post_forum
from django.conf.urls.static import static
from django.conf import settings

app_name = 'forum'
urlpatterns = [
  path('criar_novo/', create_new, name="create_new"),
  path('forum/', cont_index, name="cont_index"),
  path('post_forum/<int:id>', post_forum, name='post_forum')

]
