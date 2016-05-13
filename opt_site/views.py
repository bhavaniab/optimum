from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))
