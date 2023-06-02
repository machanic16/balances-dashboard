from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Company, Store, Rack, Shelf
from django.urls import reverse



# Create your views here.
class IndexView(ListView):
    template_name = "dashboard/index.html"
    context_object_name = "stores"

    def get_queryset(self):
        """ Just a landing page """
        return Store.objects.all()
