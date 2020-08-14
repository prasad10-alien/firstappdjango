from django.http import HttpResponse
from django.shortcuts import render
from.models import Carorder

def index(request):
    return render(request,"register.html")
def send_details(request):
    name=request.POST["name"]
    email=request.POST["email"]
    address=request.POST["address"]
    carmodel=request.POST["carmodel"]
    phoneno=request.POST["phoneno"]

    car_order=Carorder(name=name,email=email,address=address,carmodel=carmodel,phoneno=phoneno)
    car_order.save()
    return render(request,'login.html')

