from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    raw_id_fields = ['like']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['complainterator', 'address', 'contents']
    raw_id_fields = ['complainterator', 'address']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone']
    raw_id_fields = ['flats']
    search_fields = ['owner']