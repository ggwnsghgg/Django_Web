from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreate.as_view(), name="post_create"),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list/', views.list_index, name='list'),
    path("delete/<post_id>", views.delete, name="delete"),
    path("edit/<post_id>", views.edit, name="edit"),
    
   
]