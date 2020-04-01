from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # display columns
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    # clickable column
    list_display_links = ('id', 'name')
    # search field
    search_field = ('name', 'email', 'listing')
    # pagination
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
