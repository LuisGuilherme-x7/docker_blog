from django.db import models

class Thread(models.Model):

    title = models.CharField('Titulo', max_length=100,default='')
    subtitle = models.CharField('Subtitulo', max_length=100,default='')
    body = models.TextField('Mensagem', max_length=500,default='')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-modified']


class Reply(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='replies', default=True)
  reply = models.TextField('Adicionar Comentário', max_length=500,default='')

  created = models.DateTimeField('Criado em', auto_now_add=True)
  

  def __str__(self):
      return self.reply[:100]

  class Meta:
      verbose_name = 'Resposta'
      verbose_name_plural = 'Respostas'
      ordering = ['created']
