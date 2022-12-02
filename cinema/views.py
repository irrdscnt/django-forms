from django.shortcuts import get_object_or_404,render
from .models import Serie
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, FormView,DetailView
from . forms import AddForm
from django.urls import reverse
from . import parser, models, forms
from django.views import generic


def series_all(request):
    serie = Serie.objects.all()
    return render(request, 'index.html',{"serie":serie})

def delete(request, id):
   member = Serie.objects.get(id=id)
   member.delete()
   return HttpResponseRedirect(reverse('cinema:series_all'))


def find_by_id(request, id):
    series = get_object_or_404(models.Serie, id=id)
    return render(request, "detail.html", {"series": series})

class SerieDetailView(DetailView):
    model = Serie
    template_name = "detail.html"

#Post method
class AddSeries(CreateView):
   form_class = AddForm
   template_name = 'forms.html'   
   success_url = '/'

# Update method
class SerieUpdateView(UpdateView):
    model = Serie
    template_name = "update.html"
    fields = "__all__"
    success_url = '/'

#Delete method
class SerieDeleteView(DeleteView): # new
    model = Serie
    template_name = "confirm_delete.html"
    success_url = '/'

class ParserView(ListView):
    model = models.TvParser
    template_name = 'film_list.html'

    def get_queryset(self):
        return models.TvParser.objects.all()


class ParserFormView(FormView):
    template_name = 'parser_film.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Данные взяты............</h1>')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)