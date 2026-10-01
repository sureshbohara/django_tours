from django.contrib import admin
from .models import Service  

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order_level')
    search_fields = ('title',)