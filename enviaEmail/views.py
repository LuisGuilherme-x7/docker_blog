import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


def envia_email(request):
  # send_mail('Assunto 0222', 'Esse é o meu email 022222', 'teste2222@gmail.com', ['luisguilhermess15@gmail.com'])

  # return redirect('forum:cont_index')
  form = ContactForm(request.POST or None, request.FILES or None)

  if form.is_valid():    

        send_mail(form.cleaned_data['assunto'], form.cleaned_data['mensagem'], form.cleaned_data['email'], ['luisguilhermess15@gmail.com'])

        return redirect('forum:cont_index')

  else:
    print('deu errado')
    form = ContactForm()

  return render(request, 'enviaEmail/enviaEmail.html', {'form':form})
