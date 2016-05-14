from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def services(request):
    return render_to_response('services.html', {}, context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contact.html', {}, context_instance=RequestContext(request))
