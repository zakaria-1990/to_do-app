from django.contrib import admin
from .models import ToDoList, ToDoItem

# Register your models here.

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
