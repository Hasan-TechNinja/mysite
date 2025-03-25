from django.shortcuts import render, redirect
from . models import Database
from . forms import DatabaseForm

# Create your views here.

def show(request):
    data = Database.objects.all()
    context = {
        'data':data
    }
    return render(request, 'show.html', context)



def details(request, pk):
    data = Database.objects.get(id = pk)
    context = {
        'data':data
    }
    return render(request, 'details.html', context)



def create(request):
    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            pass
    else:
        form = DatabaseForm(request.POST)

    context = {
        'form':form
    }

    return render(request, 'create.html', context)



def update(request):
    return render(request, 'update.html')

