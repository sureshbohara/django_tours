from django.contrib import admin
from .models import PromoCode

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'max_uses', 'used_count', 'status')
    search_fields = ('code',)
    list_filter = ('status',)