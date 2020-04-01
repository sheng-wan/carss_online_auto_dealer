from django.contrib import admin

from .models import Listing

# customize admin columns


class ListingAdmin(admin.ModelAdmin):
    # list_display to add columns
    list_display = (
        'id',
        'vin',
        'year',
        'make',
        'model',
        'color',
        'condition',
        'price',
        'advisor',
        'is_published',
        'list_date'
    )
    # make column clickable to read individual listing
    list_display_links = (
        'id',
        'vin'
    )
    # column filter
    list_filter = (
        'advisor',
        'make',
        'year',
        'condition',
        'fuel'
    )
    # make is_published editable
    list_editable = (
        'is_published',
    )
    # search list
    search_fields = (
        'vin',
        'price'
    )
    # page pagination
    list_per_page = 25


    # register - arg1: Listing model, arg2: optional, use if you want to customize columns
admin.site.register(Listing, ListingAdmin)
