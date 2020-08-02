from django.urls import path

from views.py import views

urlpatterns = [
    path('', views.index, name='HOME'),
]