from django.contrib import admin
from .models import PackageReview

@admin.register(PackageReview)
class PackageReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'package', 'rating', 'status', 'created_at')
    list_filter = ('status', 'rating', 'package')
    search_fields = ('name', 'email', 'package__name', 'comment')
    list_editable = ('status',)
    list_per_page = 20
    date_hierarchy = 'created_at'
    actions = ['approve_reviews', 'reject_reviews']



    @admin.action(description='✅ Approve selected reviews')
    def approve_reviews(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, f'{updated} reviews approved successfully.')



    @admin.action(description='❌ Reject selected reviews')
    def reject_reviews(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, f'{updated} reviews rejected.')