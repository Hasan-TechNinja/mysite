from django.shortcuts import render, get_object_or_404
from . models import Blog

# Create your views here.

def BlogList(request):
    # data = Blog.objects.all()
    data = Blog.objects.all() 
    context = {
        'data':data
    }
    return render(request, 'blog.html', context)


def BlogDetails(request, pk):
    data = get_object_or_404(Blog, pk=pk)
    context = {
        'data':data
    }
    return render(request, 'details.html', context)