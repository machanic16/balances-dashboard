from django.contrib import admin
from .models import Company, Store, Rack, Shelf
admin.site.register([Company, Store, Rack, Shelf])