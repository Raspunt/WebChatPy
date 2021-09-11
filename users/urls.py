from django.contrib import auth
from django.urls import path 
from django.contrib.auth import views as auth_view
from .  import views

urlpatterns = [
    path("login/",auth_view.LoginView.as_view(template_name = "users/login.html"),name="startPageUrl"),
    path("reg/",views.reg,name="startPageUrl"),

]
