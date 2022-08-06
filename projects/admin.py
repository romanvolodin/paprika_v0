from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "project_preview",
        "code",
        "title",
        "deadline",
    )

    def project_preview(self, obj):
        if obj.preview:
            return mark_safe(f'<img src="{obj.preview.url}" style="width: 214px; height:135px;" />')
        else:
            return 'No preview'
    project_preview.short_description = 'Image'