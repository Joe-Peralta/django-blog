from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blogs, name='AppBlogs'),
    path('<int:id>/', views.Blog, name='blog'), 
]