
from django.urls import path 
from .  import views

urlpatterns = [
    path("",views.StartPage,name="startPageUrl"),
    path("chats/<int:chat_id>",views.ChatsPage,name="chat_id_url")    
]
