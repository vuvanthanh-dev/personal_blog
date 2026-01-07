from .models import Tag
from django.utils.text import slugify


class TagRepository:
    def get_all_tags(self):
        return Tag.objects.filter(is_active=True).order_by("name")
    
    def get_tag_by_slug(self, slug: str) -> Tag | None:
        try:
            return Tag.objects.get(slug=slug, is_active=True)
        except Tag.DoesNotExist:
            return None

    def get_tag_by_name(self, name: str) -> Tag | None:
        try:
            return Tag.objects.get(name=name, is_active=True)
        except Tag.DoesNotExist:
            return None
        
    def create_tag(self, name: str) -> Tag | None:
        try:
            return Tag.objects.create(name=name)
        except Tag.DoesNotExist:
            return None
    
    def update_tag(self, slug: str, name: str) -> Tag | None:
        tag = self.get_tag_by_slug(slug)
        if tag:
            tag.name = name
            tag.slug = slugify(name)
            tag.save()
            return tag
        return None

    def delete_tag(self, slug: str) -> bool:
        tag = self.get_tag_by_slug(slug)
        if tag:
            tag.is_active = False
            tag.save()
            return True
        return False