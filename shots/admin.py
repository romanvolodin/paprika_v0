from django.contrib import admin

from .models import ShotGroup, Shot, Version


admin.site.register(ShotGroup)
admin.site.register(Shot)
admin.site.register(Version)
