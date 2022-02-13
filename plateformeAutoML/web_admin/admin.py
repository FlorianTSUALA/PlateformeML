from django.contrib import admin

# Register your models here.

from .models import Projet

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)} 

admin.site.register(Projet, ProjetAdmin)