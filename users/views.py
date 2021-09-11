from django.http import request
from django.shortcuts import render




def login(request):
    return render(request,'users/login.html')

def reg(request):
    
    userData = request.POST
    print(userData)

    return render(request,'users/reg.html')