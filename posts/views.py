from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# URL http://127.0.0.1:9999/posts/
def index(request):
    #return HttpResponse('<marquee><h1>Welcome To My Blog Posts</h1></marquee>')
     return render(request,'index.html')

#http://127.0.0.1:9999/posts/new/
def new():
    pass