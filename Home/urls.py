
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("gallary" , views.gallary , name="Gallary"),
    path("events" , views.events , name="Events"),
    path("contacts" , views.contacts , name="Contacts"),

]