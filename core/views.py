from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView
from .models import Smartphones, Notebook
from .utils import GeraPDFMixin


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['smartphone'] = Smartphones.objects.all()
        context['notebook'] = Notebook.objects.all()
        return context


class DetalharCompraView(DetailView):
    template_name = 'detalharproduto.html'
    model = Smartphones


class DetalharCompraNoteView(DetailView):
    template_name = 'detalharprodutonote.html'
    model = Notebook



class ListaSmartPdfView(View, GeraPDFMixin):

    def get(self, request, *args, **kwargs):
        smart = Smartphones.objects.all()
        contexto = {
            'smartphone': smart,
            'quant': smart.count(),
        }
        #contexto['funcionarios'] = funcs
        #contexto['quant'] = funcs.count()
        return self.render_to_pdf('listarsmartpdf.html', contexto)


class ListaNotePdfView(View, GeraPDFMixin):

    def get(self, request, *args, **kwargs):
        note = Notebook.objects.all()
        contexto = {
            'notebook': note,
        }
        return self.render_to_pdf('listarnotepdf.html', contexto)