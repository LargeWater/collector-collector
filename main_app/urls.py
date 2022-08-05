from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('collectors/', views.collectors_index, name='collectors_index'),
  path('collectors/<int:collector_id>/', views.collectors_detail, name='collectors_detail'),
  path('collectors/create/', views.CollectorCreate.as_view(), name='collectors_create'),
  path('collectors/<int:pk>/update/', views.CollectorUpdate.as_view(), name='collectors_update'),
  path('collectors/<int:pk>/delete/', views.CollectorDelete.as_view(), name='collectors_delete'),
  path('collectors/<int:collector_id>/add_website', views.add_website, name='add_website'),
  path('followers/create/', views.FollowerCreate.as_view(), name='followers_create'),
  path('follower/<int:pk>/', views.FollowerDetail.as_view(), name='followers_detail'),
  path('followers/', views.FollowerList.as_view(), name='followers_index'),
  path('followers/<int:pk>/update/', views.FollowerUpdate.as_view(), name='followers_update'),
  path('followers/<int:pk>/delete/', views.FollowerDelete.as_view(), name='followers_delete'),
  path('collectors/<int:collector_id>/assoc_follower/<int:follower_id>/', views.assoc_follower, name='assoc_follower'),
  path('accounts/signup/', views.signup, name='signup'),
]