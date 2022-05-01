from django.contrib import admin

# Register your models here.

from .models import Projet

# class ProjetAdmin(admin.ModelAdmin):
#     list_display = ('titre', 'description',)
#     prepopulated_fields = {'slug': ('titre',)} 
# admin.site.register(Projet, ProjetAdmin)