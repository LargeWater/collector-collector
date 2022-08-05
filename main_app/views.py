from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Collector, Follower
from .forms import WebsiteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
  return render(request, 'home.html')

@login_required
def collectors_index(request):
  collectors = Collector.objects.filter(user=request.user)
  return render(request, 'collectors/index.html', {'collectors': collectors})

def collectors_detail(request, collector_id):
  collector = Collector.objects.get(id=collector_id)
  followers_collector_doesnt_have = Follower.objects.exclude(id__in = collector.followers.all().values_list('id'))
  website_form = WebsiteForm()
  return render(request, 'collectors/detail.html', {
    'collector': collector, 'website_form': website_form, 'followers': followers_collector_doesnt_have
    })

class FollowerCreate(LoginRequiredMixin, CreateView):
  model = Follower
  fields = ['name', 'color']

class FollowerList(LoginRequiredMixin, ListView):
  model = Follower

class FollowerDetail(LoginRequiredMixin, DetailView):
  model = Follower

class FollowerUpdate(LoginRequiredMixin, UpdateView):
  model = Follower
  fields = ['name', 'color']

class FollowerDelete(LoginRequiredMixin, DeleteView):
  model = Follower
  success_url = '/followers/'

class CollectorCreate(LoginRequiredMixin, CreateView):
  model = Collector
  fields = ['name', 'description']
  success_url = '/collectors/'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CollectorUpdate(LoginRequiredMixin, UpdateView):
  model = Collector
  fields = ['name', 'description']
  success_url = '/collectors/'

class CollectorDelete(LoginRequiredMixin, DeleteView):
  model = Collector
  success_url = '/collectors/'

def add_website(request, collector_id):
  form = WebsiteForm(request.POST)
  if form.is_valid():
    new_website = form.save(commit=False)
    new_website.collector_id = collector_id
    new_website.save()
  return redirect('collectors_detail', collector_id=collector_id)

def assoc_follower(request, collector_id, follower_id):
  Collector.objects.get(id=collector_id).followers.add(follower_id)
  return redirect('collectors_detail', collector_id=collector_id)

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

