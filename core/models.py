from django.db import models
from django.utils import timezone
from datetime import  datetime
from user.models import User

class Seguidor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seguido_id")
    seguid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seguidor_id")
    datetime = models.DateTimeField(default=timezone.now,blank=True)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    audio = models.FileField(upload_to='%Y/%m/%d/', blank=True)
    datetime = models.DateTimeField(default=timezone.now,blank=True)
    postador = models.ForeignKey(User , on_delete=models.CASCADE)
    editado = models.DateTimeField(default=timezone.now ,blank=True, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    conteudo = models.TextField()
    datetime = models.DateTimeField(default=timezone.now,blank=True)
    postador = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)

class Curtida(models.Model):
    curtida = models.CharField(max_length=1)
    datetime = models.DateTimeField(default=timezone.now,blank=True)
    curtidor = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)

class Curtida_comentario(models.Model):
    curtida = models.CharField(max_length=1, default='1')
    datetime = models.DateTimeField(default=timezone.now,blank=True)
    curtidor = models.ForeignKey(User , on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario , on_delete=models.CASCADE)