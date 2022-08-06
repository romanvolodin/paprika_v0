from django.contrib import admin

from .models import ShotGroup, Shot, Version


admin.site.register(ShotGroup)
admin.site.register(Version)

@admin.register(Shot)
class ShotAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "group",
        "created_by",
        "created_at",
    )
    list_filter = ("group__project", "group",)