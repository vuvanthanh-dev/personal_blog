from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseSlugModel(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)

    slug_source_field: str | None = None

    def save(self, *args, **kwargs):
        if not self.slug and self.slug_source_field:
            self.slug = slugify(getattr(self, self.slug_source_field))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class CustomQuerySet(models.QuerySet):
    def public(self):
        return self.filter(
            is_active=True,
        )