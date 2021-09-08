from typing import Text
from django.shortcuts import render
from django.http import HttpResponse
from . models import Chats,Messages
from datetime import datetime
from django.core import serializers



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



def ReturnJson(request):
    mess = Messages.objects.all()
    chats = Chats.objects.all()

    data = {
        "mess":serializers.serialize('json', mess),
        "chat":serializers.serialize('json', chats)
    }



    return HttpResponse(data["mess"], content_type='application/json')
    



