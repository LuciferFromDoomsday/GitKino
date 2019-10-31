from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html',)
