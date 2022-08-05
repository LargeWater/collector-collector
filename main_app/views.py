from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Collector


def home(request):
  return render(request, 'home.html')

def collectors_index(request):
  collectors = Collector.objects.all()
  return render(request, 'collectors/index.html', {'collectors': collectors})
  
def collectors_detail(request, collector_id):
  collector = Collector.objects.get(id=collector_id)
  return render(request, 'collectors/detail.html', {'collector': collector})


class CollectorCreate(CreateView):
  model = Collector
  fields = ['name', 'description', 'website']
