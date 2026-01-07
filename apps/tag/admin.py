from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("get_name", "slug")
    search_fields = ("name", "slug")
    readonly_fields = ("slug",)

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Tên"
    get_name.admin_order_field = "name"