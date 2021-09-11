from typing import Text
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from . models import Chats,Messages
from datetime import datetime
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.contrib import messages


def StartPage(request):

    chats = Chats.objects.all()

    if request.method == "POST":


        create_chat = request.POST.get("createChat")
        message_text = request.POST.get("textInput")
        message_name = request.POST.get("name")

        TitleChat = request.POST.get("TitleChat")
        DescChat = request.POST.get("DescChat")

        print(create_chat == 1)

        
        if message_name != None and message_text != None and create_chat == None:
            if len(Chats.objects.all()) == 0:
                Chats.objects.create(title="chat_1",disc="first_chat")

            Messages.objects.create(username=message_name,text=message_text,date=datetime.now)
        
        if create_chat == "1" and TitleChat != None and DescChat != None:
            Chats.objects.create(title=TitleChat,disc=DescChat)



    return render(request,"Polls/index.html",
    {
        "chats":chats,
    })



    



def ChatsPage(request,chat_id):

    try : 
        chat = Chats.objects.get(pk=chat_id)
        
        chats = Chats.objects.all()

        # get many to many from db
        chatMesages = chat.messages.all()


        if request.method == "POST":
            message_text = request.POST.get("textInput")
            message_name = request.POST.get("name")

            name = request.user

            if name != None and name != "":

                if  message_text != None:
                    message = Messages.objects.create(username=name,text=message_text,date=datetime.now)
                    chat.messages.add(message)
            else :
                return redirect('/login')


        return render(request,"Polls/chats.html",
        {
            "chats":chats,
            "chat":chat,
            "messages":chatMesages

        })

    except Chats.DoesNotExist:

        chats = Chats.objects.all()
        error = "чат не найден"

    
        messages.add_message(request, messages.INFO,error)


        return redirect("/")
