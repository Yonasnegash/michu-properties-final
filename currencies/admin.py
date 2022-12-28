from django.contrib import admin

from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Currency, CurrencyAdmin)