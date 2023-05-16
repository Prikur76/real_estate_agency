from django.contrib import admin

from .models import Flat

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['town', 'address', 'price', 'created_at']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
