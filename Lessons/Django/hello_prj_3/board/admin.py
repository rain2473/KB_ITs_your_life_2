import imp
from django.contrib import admin

# Register your models here.
from .models import Board
admin.site.register(Board)