from django.contrib import admin
from .models import Post  

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    search_fields = ('title',)
    list_filter = ('status',)