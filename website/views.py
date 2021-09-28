from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
from meetings.models import Meeting


class Welcome(ListView):
    model = Meeting
    template_name = 'website/welcome.html'
    context_object_name = 'meeting_list'

def date(request):
    return HttpResponse("This page was served at:" +str(datetime.now()));

def about(request):
    return HttpResponse("This is revist to this tutorial course to refresh the previously learned concept of django");

#CBV
class WebsiteView(TemplateView):
    template_name = 'view.html'

