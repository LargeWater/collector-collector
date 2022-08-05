from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('collectors/', views.collectors_index, name='collectors_index'),
  path('collectors/<int:collector_id>/', views.collectors_detail, name='collectors_detail'),
  path('collectors/create/', views.CollectorCreate.as_view(), name='collectors_create'),
]