from django.urls import path
from . import views

urlpatterns = [

    path("",views.dip2,name="dip2"),
    path("home/",views.home,name="home"),


]