from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

from core.models import BaseModel, BaseSlugModel, CustomQuerySet
from apps.category.models import Category
from apps.tag.models import Tag


class Post(BaseSlugModel, BaseModel):
    title = models.CharField(max_length=255, unique=True)
    content = CKEditor5Field(config_name="default")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="posts",
    )

    slug_source_field = "title"
    objects = CustomQuerySet.as_manager()
    
    # N-N với Category
    categories = models.ManyToManyField(
        Category,
        through="PostCategory",
        related_name="posts",
        blank=True,
    )

    # N-N với Tag
    tags = models.ManyToManyField(
        Tag,
        through="PostTag",
        related_name="posts",
        blank=True,
    )

    class Meta:
        db_table = "posts"
        indexes = [
            models.Index(fields=["slug"])
        ]
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    category = models.ForeignKey("category.Category", on_delete=models.PROTECT)

    class Meta:
        db_table = "post_categories"
        constraints = [
            models.UniqueConstraint(fields=["post", "category"], name="uq_post_category")
        ]
        indexes = [
            models.Index(fields=["category"]),
            models.Index(fields=["post"]),
        ]

    def __str__(self):
        return f"{self.post.title} - {self.category.name}"


class PostTag(models.Model):
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    tag = models.ForeignKey("tag.Tag", on_delete=models.PROTECT)

    class Meta:
        db_table = "post_tags"
        constraints = [
            models.UniqueConstraint(fields=["post", "tag"], name="uq_post_tag")
        ]
        indexes = [
            models.Index(fields=["tag"]),
            models.Index(fields=["post"]),
        ]

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"