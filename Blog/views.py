from django.shortcuts import render
from . models import Blog

# Create your views here.

def BlogList(request):
    # data = Blog.objects.all()
    data = Blog.objects.all() 
    context = {
        'data':data
    }
    return render(request, 'blog.html', context)