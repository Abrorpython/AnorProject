from django.shortcuts import render
from .models import Davlat
from django.shortcuts import redirect

def index(request):

    list = Davlat.objects.all()
    ctx = {
        'list': list
    }
    return render(request, 'main/index.html', ctx)

def create(request):
    if request.method == 'POST':
        d = Davlat(name=request.POST['name'])
        d.save()
        return redirect('index')
    return render(request, 'main/edit.html')


def update(request, id):
    try:
        d = Davlat.objects.get(id=id)
    except Davlat.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        d.name = request.POST['name']
        d.save()
        return redirect('index')
    ctx = {
        'd': d
    }
    return render(request,'main/edit.html', ctx)


def delete(request, id):
    Davlat.objects.filter(id=id).delete()
    return redirect('index')