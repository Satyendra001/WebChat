from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('<str:room>/',views.room,name='room'),
    path('getMessages/<str:room>',views.getMessages,name='getMessages'),
    path('checkview',views.checkroom, name='checkview'),
    path('send',views.send,name = 'send'),
]
