from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def events(request):
    return render(request,'events.html',{})

def booking(request):
    return render(request,'booking.html',{})

def contact(request):
    return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def login(request):
    return render(request,'login.html',{})

def signup(request):
    return render(request,'signup.html',{})

