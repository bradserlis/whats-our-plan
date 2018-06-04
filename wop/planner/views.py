from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello world.")