from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


# home page
def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, 'index.html', context)


# room page
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, 'room.html', context)
