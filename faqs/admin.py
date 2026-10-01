from django.contrib import admin
from .models import Faq 

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'order_level', 'status')
    search_fields = ('question',)
    list_filter = ('status',)