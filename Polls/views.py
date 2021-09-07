from typing import Text
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from . models import Chats,Messages
from datetime import datetime
from django.core import serializers



def StartPage(request):

    if request.method == "POST":
        message_text = request.POST.get("textInput")
        message_name = request.POST.get("name")

        Messages.objects.create(username=message_name,text=message_text,date=datetime.now)
        

    return render(request,"Polls/index.html")



def ReturnJson(request):
    mess = Messages.objects.all()
    chats = Chats.objects.all()

    data = {
        "mess":serializers.serialize('json', mess),
        "chat":serializers.serialize('json', chats)
    }



    return HttpResponse(data["mess"], content_type='application/json')
    



