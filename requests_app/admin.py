from django.contrib import admin
from .models import AssetRequest

@admin.register(AssetRequest)
class AssetRequestAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'product', 'quantity', 'status', 'date_submitted', 'required_by_date')
    list_filter = ('status', 'date_submitted', 'user')
    search_fields = ('product', 'description', 'user__username')
    actions = ['mark_approved', 'mark_rejected']
    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'HOD'

    def mark_approved(self, request, queryset):
        queryset.update(status='Approved')
    mark_approved.short_description = "Mark selected requests as Approved"

    def mark_rejected(self, request, queryset):
        queryset.update(status='Rejected')
    mark_rejected.short_description = "Mark selected requests as Rejected"

    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('user', 'product', 'asset_price', 'tentative_vendor', 'required_by_date', 'quantity', 'description', 'date_submitted')
        return []
