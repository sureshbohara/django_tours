from django.contrib import admin
from .models import Assignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('package', 'staff', 'start_date', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('package__name', 'staff__name')