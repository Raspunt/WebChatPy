

from django.urls import path 

from .  import views

urlpatterns = [
    path("",views.StartPage,name="startPageUrl"),
    path("messages/",views.ReturnJson ,name="messageJsonUrl")    
]
