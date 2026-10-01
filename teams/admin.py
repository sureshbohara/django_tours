from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order_level', 'status')
    search_fields = ('name',)
    list_filter = ('role', 'status')