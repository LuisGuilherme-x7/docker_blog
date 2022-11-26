from django.urls import path
from . import views

app_name = 'enviaEmail'
urlpatterns = [
  path('', views.envia_email, name="enviaEmail"),
 

]
