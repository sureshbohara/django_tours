from django.contrib import admin
from .models import SiteSetting, DiskUsageLog

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('system_name', 'email', 'phone')

@admin.register(DiskUsageLog)
class DiskUsageLogAdmin(admin.ModelAdmin):
    list_display = ('log_date', 'used_bytes', 'free_bytes')
    readonly_fields = ('log_date', 'used_bytes', 'free_bytes')