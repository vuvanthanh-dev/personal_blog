from .models import Tag


class TagRepository:
    def get_all_tags(self):
        return Tag.objects.all().order_by("name")
    
    def get_tag_by_slug(self, slug: str) -> Tag | None:
        try:
            return Tag.objects.get(slug=slug)
        except Tag.DoesNotExist:
            return None

    def get_tag_by_name(self, name: str) -> Tag | None:
        try:
            return Tag.objects.get(name=name)
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
            tag.save()
            return tag
        return None

    def delete_tag(self, slug: str) -> bool:
        tag = self.get_tag_by_slug(slug)
        if tag:
            tag.delete()
            return True
        return False