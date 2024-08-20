from django.contrib import admin
from .models import Listing, PropertyMultiplePhoto
from .forms import ShowAdminForm
from django.template.loader import get_template
from django.utils.translation import gettext as _

class ShowPhotoInline(admin.TabularInline):
    model = PropertyMultiplePhoto
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("admin/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Thumbnail")

@admin.register(Listing)
class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm
    inlines = [ShowPhotoInline]
    list_display = ('id', 'title', 'is_published', 'is_featured','price', 'is_for_rent', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published', 'is_featured', 'is_for_rent')
    search_fields = ('title', 'description', 'address', 'city', 'price')
    list_per_page = 25
    # fields = ('realtor', 'title', 'address', 'city', 'description', 'video', 'photo_main', 'list_date')

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)