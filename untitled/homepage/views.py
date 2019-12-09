from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html',)

# def register(request):
#     form = UserCreationForm()
#     return render(request,'homepage/templates/registration/register.html', {'form':form})



def cities_list(request):
    city_list = City.objects.order_by('id')[:20]
    return render(request, 'home.html', {'city_list': city_list})
