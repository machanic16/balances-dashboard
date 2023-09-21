from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Company, Store, Rack, Shelf
from django.urls import reverse

# DjangoRest 
from django.http import JsonResponse
from .models import Company, Store,Rack, Shelf
from .serializers import CompanySerializer, StoreSerializer,RackSerializer,ShelfSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#Function views 
@api_view(['GET','POST'])
def store_list(request,format=None):
    #   Get all the stores 
    #   Serialize then 
    #   Return json 
    if request.method == 'GET':
        store = Store.objects.all()
        serializer = StoreSerializer(store,many=True)
        return JsonResponse({'data':serializer.data})
    
    if request.method == 'POST':
        serializer = StoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)




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