from django.contrib import admin

from .models import Advisor


class AdvisorAdmin(admin.ModelAdmin):
    # display columns
    list_display = (
        'id',
        'name',
        'email',
        'hire_date'
    )
    # clickable columns
    list_display_links = (
        'id',
        'name'
    )
    # search field
    search_field = (
        'name',
    )
    # pagination
    list_per_page = 25


# register
admin.site.register(Advisor, AdvisorAdmin)
