from django.contrib import admin

# Register your models here.
from .models import profile, Location

class profileAdmin(admin.ModelAdmin):
    pass
class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(profile, profileAdmin)
admin.site.register(Location, LocationAdmin)