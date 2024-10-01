from django.shortcuts import render, redirect
from django.contrib import messages
from .import global_msg
from .models import Csit

# Create your views here.
def index(request):
    data=Csit.objects.all()
    return render(request,"npjairport/table.html",{'data':data})

def base(request):
    return render(request,"npjairport\Base.html")

def about(request):
    return render(request,"npjairport\About.html")

def contact(request):
    return render(request,"npjairport\contact.html")

def table(request):
    data = Csit.objects.filter(is_delete=False)
    return render(request,"npjairport/table.html",{'data':data})


def form(request):
    if request.method=="POST":
        det= request.POST
        name=det.get("name")
        email=det.get("email")
        phone=det.get("phone")
        address=det.get("address")
        Csit.objects.create(name=name, email=email, phone=phone, address=address)
        messages.success(request,global_msg.SUCCESS_MESSAGE)
    return render(request,"npjairport/form.html")

def edit(request, pk):
    if request.method == 'POST':
        det = request.POST
        name = det.get('name')
        phone = det.get('phone')
        email = det.get('email')
        address = det.get('address')
        dm = Csit.objects.get(id=pk, is_delete=True)
        dm.name = name
        dm.phone = phone
        dm.email = email
        dm.address=address
        dm.save()

        return redirect('/')
    dt = Csit.objects.get(id=pk)
    return render(request, "npjAirport/edit.html", {'dt':dt})

def delete(request, pk):
  dx =  Csit.objects.get(id=pk, is_delete="False")
  dx.is_delete=True
  dx.save()
  messages.success(request, global_msg.DELETE_MESSAGE)
  return redirect('/')

