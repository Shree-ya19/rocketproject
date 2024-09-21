from django.shortcuts import render, redirect
from .models import Csit

# Create your views here.
def index(request):
    data=Csit.objects.all()
    return render(request,"npjairport\index.html",{'data':data})

def base(request):
    return render(request,"npjairport\Base.html")

def about(request):
    return render(request,"npjairport\About.html")

def contact(request):
    return render(request,"npjairport\contact.html")

def table(request):
    data = Csit.objects.all()
    return render(request,"npjairport/table.html",{'data':data})


def form(request):
    if request.method=="POST":
        det= request.POST
        name=det.get("name")
        email=det.get("email")
        phone=det.get("phone")
        Csit.objects.create(name=name, email=email, phone=phone)
    return render(request,"npjairport/form.html")

def edit(request, pk):
    if request.method == 'POST':
        det = request.POST
        name = det.get('name')
        phone = det.get('phone')
        email = det.get('email')
        dm = Csit.objects.get(id=pk)
        dm.name = name
        dm.mob = phone
        dm.email = email
        dm.save()
        return redirect('/')
    dt = Csit.objects.get(id=pk)
    return render(request, "npjAirport/edit.html", {'dt':dt})
