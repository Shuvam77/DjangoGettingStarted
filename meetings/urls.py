"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import Detail, RoomList
from . import views

urlpatterns = [
    path('<int:pk>', Detail.as_view(), name='detail'),
    path('room_list', RoomList.as_view(), name='room_list'),
    path('addNew', views.addNew, name='addNew'),
    path('newroom', views.newroom, name='newroom'),
    path('edit_room/<int:id>', views.edit_Room, name='edit_room'),
    path('delete_room/<int:id>', views.delete_Room, name="delete_room"),

]
