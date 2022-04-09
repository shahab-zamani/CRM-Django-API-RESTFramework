from django.contrib import admin
from .models import Leads

# admin.site.register(Leads)


@admin.register(Leads)
class LeadsAdmin (admin.ModelAdmin):
    list_filter = ('firstName', 'lastName')
