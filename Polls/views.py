from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from . models import Chats,Messages
from datetime import datetime
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from WebChat.consumers import ChatConsumer


def StartPage(request):

    # получаем информацию из базы данных
    chats = Chats.objects.all()


    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'chat',
        {
            'type': 'chat.message',
            'message': 'Test message'
        }
    )



    # проверяем это POST запрос
    if request.method == "POST":

        #  получаем информацию из Post запроса
        TitleChat = request.POST.get("TitleChat")
        DescChat = request.POST.get("DescChat")
        
        # берем username из запроса
        name = request.user


        # создание чата

        # проверяем пользователь авторизован
        if name != None and name != "" and  TitleChat != "" :
            Chats.objects.create(title=TitleChat,disc=DescChat)
        else:
            return redirect('/login')




    return render(request,"Polls/index.html",
    {
        "chats":chats,
    })



def Get_Json(request):

    messages = list(Messages.objects.values())
    chats =  list(Chats.objects.values())

    return JsonResponse(
    {
        "messages":messages,
        'chats':chats,
    },status =200)



def vue_index(request):
    
    return render(request,"Polls/vue_index.html")



def ChatsPage(request,chat_id):

    try : 

        # получаем информацию из базы данных
        chat = Chats.objects.get(pk=chat_id) 
        chats = Chats.objects.all()
    
        # берем сообшения(many to many) из чата
        chatMesages = chat.messages.all()

     

        # проверяем это POST запрос
        if request.method == "POST":

            #  получаем информацию из Post запроса
            message_text = request.POST.get("textInput")
            TitleChat = request.POST.get("TitleChat")
            DescChat = request.POST.get("DescChat")

            print(request.POST)

            # создаем чат
            if TitleChat != None :
                Chats.objects.create(title=TitleChat,disc=DescChat)



            # берем username из запроса
            name = request.user
            if name != None and name != "" :
                if  message_text != "" and message_text != None: #  имя не пустое
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

    except Chats.DoesNotExist: # зашита от гениев 
        
        # если пользователь в адресную строку напишет не сушествующий чат,
        # его перекинет на главную страницу

        chats = Chats.objects.all()
        error = "чат не найден"

        messages.add_message(request, messages.INFO,error)


        return redirect("/")
