from django.contrib.gis import admin

from listings.models import SpotFix, Location
# Register your models here.
# admin.site.register(SpotFix)


class SpotFixAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SpotFixAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

admin.site.register(SpotFix)
admin.site.register(Location)
