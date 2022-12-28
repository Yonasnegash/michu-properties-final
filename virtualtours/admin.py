from django.contrib import admin
from .models import VirtualTour, VirtualTourPhotos
from .forms import ShowAdminForm
from django.template.loader import get_template
from django.utils.translation import gettext as _

class ShowPhotoInline(admin.TabularInline):
    model = VirtualTourPhotos
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("admin/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Thumbnail")

@admin.register(VirtualTour)
class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm
    inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)
