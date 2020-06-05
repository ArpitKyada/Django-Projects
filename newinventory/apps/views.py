from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    a = Desktop.objects.all()
    b = Laptop.objects.all()
    c = Mobile.objects.all()
    
    context = {'a':a, 'b':b, 'c':c}
    return render(request, 'apps/index.htm', context)


def show_Device(request, cls, header):
    form = cls.objects.all()

    context={'form':form,
            'header' : header
        }
    return render(request, 'apps/index.htm', context)

def show_desktop(request):
    return show_Device(request, Desktop, 'Desktop')

def show_laptop(request):
    return show_Device(request, Laptop, 'Laptop')

def show_mobile(request):
    return show_Device(request, Mobile, 'Mobile')

def create_device(request, cls):
    if request.method == "GET":   
         form = cls()
    else:
        form = cls(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'apps/create_item.htm', context)

def create_desktop(request):
    return create_device(request, DesktopForm)

def create_laptop(request):
    return create_device(request, LaptopForm)

def create_mobile(request):
    return create_device(request, MobileForm)


def update_device(request, id, cls, clsform):
    if request.method == "GET":
        obj = cls.objects.get(pk=id)
        form = clsform(instance=obj)
    else:
        obj = cls.objects.get(pk=id)
        form = clsform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'apps/create_item.htm',context)

def update_desktop(request, id):
    return update_device(request, id, Desktop, DesktopForm)

def update_laptop(request, id):
    return update_device(request, id, Laptop, LaptopForm)

def update_mobile(request, id):
    return update_device(request, id, Mobile, MobileForm)

def delete_device(request, id, cls):
    cls.objects.get(pk = id).delete()
    return redirect("home")

def delete_desktop(request, id):
    return delete_device(request, id, Desktop)

def delete_laptop(request, id):
    return delete_device(request, id, Laptop)

def delete_mobile(request, id):
    return delete_device(request, id, Mobile)
