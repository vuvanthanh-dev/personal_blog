from django.contrib import admin

from .models import Post, PostCategory, PostTag


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    inlines = [PostCategoryInline, PostTagInline]