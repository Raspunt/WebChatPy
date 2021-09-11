from django.urls import path 

from .  import views

urlpatterns = [
    path("login/",views.login,name="startPageUrl"),
    path("reg/",views.reg,name="startPageUrl"),

]
