from django.shortcuts import render, redirect, get_object_or_404
from . models import Database
from . forms import DatabaseForm


# Create your views here.

def show(request):
    data = Database.objects.all()
    context = {
        'data':data
    }
    return render(request, 'show.html', context)



def detailsView(request, pk):
    data = Database.objects.get(id = pk)
    context = {
        'data':data
    }
    return render(request, 'Tdetails.html', context)



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



def update(request, pk):
    data = get_object_or_404(Database, id = pk)

    if request.method == 'POST':
        form = DatabaseForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("home")
        pass
    form = DatabaseForm(instance=data)


    context = {
        'form':form
    }

    return render(request, 'update.html', context)



def deleteView(request, pk):
    data = get_object_or_404(Database, id = pk)
    data.delete()
    return redirect('home')