from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import parser, models, forms

class ParserView(ListView):
    model = models.Laptop
    template_name = 'laptop_list.html'

    def get_queryset(self):
        return models.Laptop.objects.all()

class ParserFormView(FormView):
    template_name = 'parser_laptops.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Данные получены.......</h1>')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)