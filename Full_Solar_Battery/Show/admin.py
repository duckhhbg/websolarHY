from django.contrib import admin
from .models import Manager_Model

# Register your models here.
@admin.register(Manager_Model)
class Manager_Admin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'userName', 'Jurisdiction')