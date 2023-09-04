from django.contrib import admin
from .models import *

@admin.register(Product)
class Proudct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price',]
    list_filter = ['name', 'price',]
    
