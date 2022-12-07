from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import HomeView, ListaSmartPdfView, ListaNotePdfView, DetalharCompraView, DetalharCompraNoteView

app_name = 'core'
urlpatterns = [
    path('listasmartpdf/', ListaSmartPdfView.as_view(),
         name='Listar_smart_pdf'),
    path('listanotepdf/', ListaNotePdfView.as_view(),
         name='Listar_note_pdf'),
    path('<int:pk>/', DetalharCompraView.as_view(), name='detalhar_prod'),
    path('note/<int:pk>/', DetalharCompraNoteView.as_view(), name='detalhar_prod_note')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)