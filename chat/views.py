from django.core.checks import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from chat import models
from chat.models import Room, Message

# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)

    return render(request,'room.html',{'room':room,'username':username,'room_details':room_details})

def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    username = request.POST['username'] 
    room_id = request.POST['room_id']
    message = request.POST['message']

    new_message = Message.objects.create(user = username,value = message, room = room_id)
    new_message.save()
    
    return HttpResponse('Message Sent Successfully')


def getMessages(request,room):
    room_details = Room.objects.get(name = room)

    messages = Message.objects.filter(room = room_details.id)
    print(messages.values())
    return JsonResponse({'messages':list(messages.values())})