from django.contrib.auth.models import User
from django.db import models
from django_cpf_cnpj.fields import CNPJField
from stdimage.models import StdImageField

class Marca(models.Model):
    razaosocial = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    cnpj = CNPJField(masked=True)

    class Meta:
        ordering = ['razaosocial']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.razaosocial


class Smartphones(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE, related_name='Marca_Smartphone')
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.CharField(max_length=500)
    preco = models.FloatField()
    imagem = StdImageField(upload_to='smartphonepics', variations={'thumbnail':{'width': 1000, 'height': 667, 'crop': True}})
    texto = models.TextField(max_length=1000)
    estoque = models.IntegerField()
    cliente = models.ManyToManyField(User, related_name='cliente_smartphone', blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Smartphone'
        verbose_name_plural = 'Smartphones'

    def __str__(self):
        return self.nome


class Notebook(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE, related_name='Marca_Notebook')
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.CharField(max_length=500)
    preco = models.FloatField()
    imagem = StdImageField(upload_to='notebookpics', variations={'thumbnail':{'width': 600, 'height': 600, 'crop': True}})
    texto = models.TextField(max_length=1000)
    estoque = models.IntegerField()
    cliente = models.ManyToManyField(User, related_name='cliente_notebook', blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebook'

    def __str__(self):
        return self.nome




