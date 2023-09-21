from rest_framework import serializers
from .models import Company, Store,Rack, Shelf

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id',
                  'name',
                  'parent_company'
                  ]

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id',
                  'name',
                  'city',
                  'state',
                  'country',
                  'company'
                  ]

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = ['id',
                  'name',
                  'store',
                  'status']


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id',
                  'rack',
                  'min_weight',
                  'max_weight'
                  ]





