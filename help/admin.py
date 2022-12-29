from django.contrib import admin
from .models import Help

class HelpAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','email','message',)
    list_display_links = ('id', 'fullname')
    search_fields = ('email',)
    list_per_page = 25
    
admin.site.register(Help, HelpAdmin)
