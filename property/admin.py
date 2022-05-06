from django.contrib import admin
from property.models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("owner", )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    inlines = [
        FlatsInline,
    ]
    list_editable = ('new_building', )
    list_filter = ('new_building', )
    raw_id_fields = ('liked_by', )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = ('user', 'flat', 'complaint_text')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone')


