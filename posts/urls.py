from django.urls import path
from . import views 

# /posts
urlpatterns = [
  path('',views.index),
]