from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def categories(request):
    return render(request,'categories.html')