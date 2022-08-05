from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Collector, Follower
from .forms import WebsiteForm


def home(request):
  return render(request, 'home.html')

def collectors_index(request):
  collectors = Collector.objects.all()
  return render(request, 'collectors/index.html', {'collectors': collectors})

def collectors_detail(request, collector_id):
  collector = Collector.objects.get(id=collector_id)
  website_form = WebsiteForm()
  return render(request, 'collectors/detail.html', {
    'collector': collector, 'website_form': website_form
    })

class FollowerCreate(CreateView):
  model = Follower
  fields = ['name', 'color']

class FollowerList(ListView):
  model = Follower

class FollowerDetail(DetailView):
  model = Follower

class FollowerUpdate(UpdateView):
  model = Follower
  fields = ['name', 'color']

class FollowerDelete(DeleteView):
  model = Follower
  success_url = '/followers/'

class CollectorCreate(CreateView):
  model = Collector
  fields = ['name', 'description', 'website']
  success_url = '/collectors/'

class CollectorUpdate(UpdateView):
  model = Collector
  fields = ['name', 'description', 'website']
  success_url = '/collectors/'

class CollectorDelete(DeleteView):
  model = Collector
  success_url = '/collectors/'

def add_website(request, collector_id):
  form = WebsiteForm(request.POST)
  if form.is_valid():
    new_website = form.save(commit=False)
    new_website.collector_id = collector_id
    new_website.save()
  return redirect('collectors_detail', collector_id=collector_id)
