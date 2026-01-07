from django.contrib import admin

from .models import Post, PostCategory, PostTag, Category, Tag


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("get_title", "get_author", "get_categories", "get_tags")
    readonly_fields = ("slug",)
    inlines = [PostCategoryInline, PostTagInline]

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = "Categories"
    get_categories.admin_order_field = "categories"

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = "Tags"
    get_tags.admin_order_field = "tags"

    def get_author(self, obj):
        return obj.author.username
    get_author.short_description = "Tác giả"
    get_author.admin_order_field = "author"

    def get_title(self, obj):
        return obj.title
    get_title.short_description = "Tiêu đề"
    get_title.admin_order_field = "title"