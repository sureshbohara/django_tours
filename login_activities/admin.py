from django.contrib import admin
from .models import LoginActivity

@admin.register(LoginActivity)
class LoginActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'os', 'browser', 'device_type', 'login_at', 'logout_at')
    list_filter = ('device_type',)
    search_fields = ('user__username', 'ip_address')
    readonly_fields = ('user', 'ip_address', 'user_agent', 'os', 'browser', 'device_type', 'login_at')