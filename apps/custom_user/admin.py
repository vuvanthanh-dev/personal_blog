from django.contrib import admin

from apps.custom_user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "get_full_name")
    search_fields = ("username", "email")

    def get_full_name(self, obj):
        return obj.full_name
    get_full_name.short_description = "Họ và tên"
    get_full_name.admin_order_field = "full_name"