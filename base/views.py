from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


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


# create room page
def create_room(request):
    form = RoomForm()
    context = {"form": form}
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        return render(request, 'room_form.html', context)


# update room page
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    context = {"form": form}
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        return render(request, 'room_form.html', context)
