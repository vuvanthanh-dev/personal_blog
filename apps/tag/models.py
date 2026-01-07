from django.db import models
from core.models import BaseModel, BaseSlugModel


class Tag(BaseSlugModel, BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug_source_field = "name"

    class Meta:
        db_table = "tags"
        indexes = [
            models.Index(fields=["slug"], name="tag_slug_idx"),
        ]
        ordering = ("-created_at",)

    def __str__(self):
        return self.name