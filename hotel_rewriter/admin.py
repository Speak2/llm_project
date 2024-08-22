from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    # class Media:
    #     css = {
    #         'all': ('css/custom_admin.css',)
    #     }
    list_display = ('property_id', 'title',
                    'create_date', 'update_date')
    list_display_links = ('title',)
    ordering = ('property_id',)
    list_filter = ('create_date', 'update_date')
    search_fields = ('property_id', 'title', 'description')
    readonly_fields = ('create_date', 'update_date')

    fieldsets = (
        ('Property Details', {
            'fields': ('property_id', 'title', 'description')
        }),
        ('Timestamps', {
            'fields': ('create_date', 'update_date'),
            'classes': ('collapse',)
        }),
    )
