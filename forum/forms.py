from django import forms
from django.forms import ModelForm
from .models import Thread, Reply

class CreateForm(ModelForm):
    class Meta:
        model = Thread
        fields = [
            'title',
            'subtitle',
            'body',
               
        ]

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = [
            'reply',
        ]
