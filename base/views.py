from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q


# home page
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(
        title__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics}
    return render(request, 'index.html', context)


# room page
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, 'room.html', context)


# create room
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


# update room
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


# delete room
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"name": room}
    if request.method == 'POST':
        room.delete()
        return redirect("home")
    return render(request, 'delete.html', context)
