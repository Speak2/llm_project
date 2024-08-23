from django.contrib import admin
from django.utils.html import format_html
from .models import Property, PropertySummary


class PropertySummaryInline(admin.StackedInline):
    model = PropertySummary
    can_delete = False
    extra = 0


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'title',
                    'description_preview', 'create_date', 'update_date')
    list_display_links = ('title',)
    ordering = ('property_id',)
    list_filter = ('create_date', 'update_date')
    search_fields = ('property_id', 'title', 'description')
    readonly_fields = ('create_date', 'update_date')
    inlines = [PropertySummaryInline]

    fieldsets = (
        ('Property Details', {
            'fields': ('property_id', 'title', 'description'),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('create_date', 'update_date'),
            'classes': ('collapse',)
        }),
    )

    def description_preview(self, obj):
        return format_html(
            '<span title="{}">{}</span>',
            obj.description,
            obj.description[:50] + '...' if len(obj.description) > 50
            else obj.description
        )
    description_preview.short_description = 'Description'


@admin.register(PropertySummary)
class PropertySummaryAdmin(admin.ModelAdmin):
    list_display = ('get_property_id', 'get_property_title',
                    'summary_preview', 'created_at', 'updated_at')
    list_display_links = ('get_property_title',)
    ordering = ('property__id',)
    list_filter = ('created_at', 'updated_at')
    search_fields = ('property__title', 'summary')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Property Information', {
            'fields': ('property',)
        }),
        ('Summary', {
            'fields': ('summary',),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_property_title(self, obj):
        return obj.property.title
    get_property_title.short_description = 'Property Title'
    get_property_title.admin_order_field = 'property__title'

    def get_property_id(self, obj):
        return obj.property.property_id
    get_property_id.short_description = 'Property ID'
    get_property_id.admin_order_field = 'property__property_id'

    def summary_preview(self, obj):
        return format_html(
            '<span title="{}">{}</span>',
            obj.summary, obj.summary[:50] + '...' if len(obj.summary) > 50
            else obj.summary)
    summary_preview.short_description = 'Summary'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "property":
            kwargs["queryset"] = Property.objects.all().order_by('title')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['property'].label_from_instance = (
            lambda obj: obj.title
        )
        return form
