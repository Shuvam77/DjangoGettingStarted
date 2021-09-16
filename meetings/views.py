from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .RoomForm import RoomForm

# Create your views here.
from meetings.models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk = id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

#Class
MeetingForm = modelform_factory(Meeting, exclude=[])

def addNew(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/addNew.html", {'form': form})

def room_list(request):
    return render(request, "meetings/roomList.html", {"rooms": Room.objects.all()})

def newroom(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = RoomForm()
    return render(request, "meetings/newroom.html", {"form": form})

def edit_Room(request, id):
    room = get_object_or_404(Room, pk=id)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    context = {"form": form}
    return render(request, "meetings/edit_room.html", context)

def delete_Room(request, id):
    room = get_object_or_404(Room, pk=id)
    if request.method == "POST":
        room.delete()
        return redirect("welcome")

    context = {"room": room}
    return render(request, "meetings/delete.html", context)