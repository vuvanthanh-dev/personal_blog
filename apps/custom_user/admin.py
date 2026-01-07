from django.contrib import admin

from apps.custom_user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "full_name")
    search_fields = ("username", "email")