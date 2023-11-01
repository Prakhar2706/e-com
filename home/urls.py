from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.loginuser , name='login'),
    path("home", views.index , name='home'),
    path("about", views.about , name='about'),
    path("services", views.services , name='services'),
    path("contact", views.contact , name='contact'),
    path("stationary", views.stationary , name='stationary'),
    path("phone_covers", views.phone_covers , name='phone_covers'),
    path("bags", views.bags , name='bags'),
    path("muchmore", views.muchmore , name='muchmore'),
    path("login", views.loginuser , name='login'),
    path("logout", views.logoutuser , name='logout'),
    path("register", views.register , name='register'),
]