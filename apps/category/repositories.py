from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q

from core.constants.paginator import (
    PAGE_DEFAULT,
    PAGE_SIZE_DEFAULT,
    PAGE_SIZE_MAX,
)

from .models import Category


class CategoryRepository:
    def get_all_categories(self, query_params: dict | None = None):
        page_index = int(
            query_params.get("pageIndex", PAGE_DEFAULT)
            if query_params
            else PAGE_DEFAULT
        )
        page_size = int(
            query_params.get("pageSize", PAGE_SIZE_DEFAULT)
            if query_params
            else PAGE_SIZE_DEFAULT
        )
        name = (
            query_params.get("name", "")
            if query_params
            else ""
        )
        slug = (
            query_params.get("slug", "")
            if query_params
            else ""
        )

        if page_size > PAGE_SIZE_MAX:
            page_size = PAGE_SIZE_MAX

        query = Q()

        if name:
            query &= Q(name__icontains=name)

        if slug:
            query &= Q(slug__icontains=slug)
        
        try:
            categories_qs = (
                Category.objects.filter(query)
                .only("id", "name", "slug", "created_at", "updated_at")
            )
            paginator = Paginator(categories_qs, page_size)
            page_obj = paginator.page(page_index)
        except EmptyPage:
            return {
                "items": [],
                "total_records": paginator.count,
                "page_index": page_index,
                "page_size": page_size,
                "total_pages": paginator.num_pages,
            }

        return {
            "items": page_obj.object_list,
            "total_records": paginator.count,
            "page_index": page_obj.number,
            "page_size": page_size,
            "total_pages": paginator.num_pages,
        }
    
    def get_category_by_slug(self, slug: str) -> Category | None:
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None
    
    def get_category_by_name(self, name: str) -> Category | None:
        try:
            return Category.objects.get(name=name)
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