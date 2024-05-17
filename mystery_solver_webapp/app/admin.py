from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Stories)
class Mystery_Stories(admin.ModelAdmin):
    list_display=['pk']
