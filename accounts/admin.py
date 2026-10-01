from django.contrib import admin
from .models import AdminUser

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'status', 'last_login_at')
    search_fields = ('name', 'email')
    list_filter = ('status',)