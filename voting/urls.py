from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('vote/<int:position_id>', views.vote, name = 'vote'),
    path('unvote/', views.unvote, name = 'unvote'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
  
  ]