from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order_level') 
    search_fields = ('title',) 
    list_filter = ('status',) 
    list_editable = ('status', 'order_level') 