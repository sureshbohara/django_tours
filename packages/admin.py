from django.contrib import admin
from .models import Package, FixedDeparture

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'trip_price', 'status', 'order_level')
    search_fields = ('name',)
    list_filter = ('status',)

@admin.register(FixedDeparture)
class FixedDepartureAdmin(admin.ModelAdmin):
    list_display = ('package', 'start_date', 'end_date', 'status')
    list_filter = ('status',)