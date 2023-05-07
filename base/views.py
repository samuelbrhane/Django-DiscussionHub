from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {
        "id": 1, "title": "Frontend web development",
    },
    {
        "id": 2, "title": "Backend web development",
    },
    {
        "id": 3, "title": "Learn python and django"
    }
]


# home page
def home(request):
    context = {"rooms": rooms}
    return render(request, 'index.html', context)

# room page


def room(request, pk):
    current_room = None
    for room in rooms:
        if room["id"] == int(pk):
            current_room = room

    context = {"room": current_room}
    return render(request, 'room.html', context)
