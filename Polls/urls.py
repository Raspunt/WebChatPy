
from django.urls import path 
from .  import views

urlpatterns = [
    path("",views.StartPage,name="startPageUrl"),
    path("chats/<int:chat_id>",views.ChatsPage,name="chat_id_url"),
    path("vue/",views.vue_index,name ="vueUrl"),
    path("jsonData/",views.Get_Json,name="JsonUrl")
]
