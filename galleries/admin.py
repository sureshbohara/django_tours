from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_on', 'status')  
    search_fields = ('name',)
    list_filter = ('status',)