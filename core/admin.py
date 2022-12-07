from django.contrib import admin
from .models import Marca, Smartphones, Notebook


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['razaosocial', 'slug', 'cnpj']
    prepopulated_fields = {'slug':('razaosocial',)}


@admin.register(Smartphones)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'marca', 'descricao', 'preco', 'imagem', 'texto']
    prepopulated_fields = {'slug':('nome',)}
    list_filter = ['nome', 'marca', 'preco']


@admin.register(Notebook)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'marca', 'descricao', 'preco', 'imagem', 'texto']
    prepopulated_fields = {'slug':('nome',)}
    list_filter = ['nome', 'marca', 'preco']


