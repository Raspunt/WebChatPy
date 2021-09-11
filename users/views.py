from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def reg(request):
    
    error = ""
    if request.method == "POST": # если страница отправляет POST то


        #  Берем информацию из POST
        userName = request.POST.get("UserName") 
        Email = request.POST.get("Email")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")

        # Проверяем пароль 
        if password_1 != password_2 :
            error = "Password mismatch"
            print("пароли не совпадают")
        else:
            print("пароли совпадают")    

            # создаем пользователя без пароля
            user = User(username=userName,email=Email)

            # set_password  зашифровывает пароль сверху если вставить шифровки не будет
            user.set_password(password_1)
            user.save()

            redirect("/")



    return render(request,'users/reg.html',
    {
        "error":error
    })