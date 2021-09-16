from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request, 'website/welcome.html', {'meetings': Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at:" +str(datetime.now()));

def about(request):
    return HttpResponse("This is revist to this tutorial course to refresh the previously learned concept of django");

#CBV
class WebsiteView(TemplateView):
    template_name = 'view.html'

