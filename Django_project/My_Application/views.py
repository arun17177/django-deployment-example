from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import datas

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()

    return render(request,"home.html")

def view(request):
    mydata = datas.objects.all()
    return render(request,"view.html",{'datas':mydata})

def update(request,id):
    mydata=datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('/view')

    return render(request,"update.html",{'data':mydata})

def delete(request,id):
    mydata=datas.objects.get(id=id)
    mydata.delete()
    return redirect('/view')