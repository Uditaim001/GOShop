from django.shortcuts import render ,redirect
from Home.models import Contacts
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    context={
        'variable':"This is Fine"
    }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")
def contacts(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address=request.POST.get('address')
        desc=request.POST.get('desc')
        contact=Contacts(name=name,email=email,phone=phone,address=address,desc=desc)
        contact.save()
    return render(request,'contacts.html')
    #return HttpResponse("this is contact page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")        
def loginUser(request):
    # if request.method=="POST":

    return render(request,'login.html')
def logoutUser(request):
    return render(request,'index.html')
