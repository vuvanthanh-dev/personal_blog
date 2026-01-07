from django.utils.text import slugify

from .models import Category


class CategoryRepository:
    def get_all_categories(self):
        return Category.objects.filter(is_active=True).order_by("name")
    
    def get_category_by_slug(self, slug: str) -> Category | None:
        try:
            return Category.objects.get(slug=slug, is_active=True)
        except Category.DoesNotExist:
            return None
    
    def get_category_by_name(self, name: str) -> Category | None:
        try:
            return Category.objects.get(name=name, is_active=True)
        except Category.DoesNotExist:
            return None
        
    def create_category(self, name: str) -> Category | None:
        try:
            return Category.objects.create(name=name)
        except Category.DoesNotExist:
            return None
    
    def update_category(self, slug: str, name: str) -> Category | None:
        category = self.get_category_by_slug(slug)
        if category:
            category.name = name
            category.slug = slugify(name)
            category.save()
            return category
        return None
    
    def delete_category(self, slug: str) -> bool:
        category = self.get_category_by_slug(slug)
        if category:
            category.is_active = False
            category.save()
            return True
        return False