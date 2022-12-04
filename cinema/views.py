from django.shortcuts import get_object_or_404,render
from .models import Serie
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, FormView,DetailView
from . forms import AddForm
from django.urls import reverse
from . import models, forms
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
