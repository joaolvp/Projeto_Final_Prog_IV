from django.urls import path
from clientes import views
from clientes.views import CadastroClienteView

app_name = "clientes"

urlpatterns =[
    path('cadastrar/', CadastroClienteView.as_view(), name='cadastro_cliente')
]