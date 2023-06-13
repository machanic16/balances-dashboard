from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Company, Store, Rack, Shelf
from django.urls import reverse



class IndexView(ListView):
    template_name = "dashboard/index.html"
    context_object_name = "stores"

    def get_queryset(self):
        """ Just a landing page """
        return Store.objects.all()
    

class StoreView(generic.DetailView):
    template_name = 'dashboard/store_view.html'
    model = Store
    context_object_name = "store"

    # def get_queryset(self) -> QuerySet[Any]:
    #     return get_object_or_404(Store,pk=)