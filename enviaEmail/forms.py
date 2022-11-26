from django import forms

class ContactForm(forms.Form):
  assunto = forms.CharField(max_length=255)
  email = forms.EmailField()
  mensagem = forms.CharField(widget=forms.Textarea)
