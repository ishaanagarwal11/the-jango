from django.contrib import admin
from .models import Prep

class PrepAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Prep, PrepAdmin)