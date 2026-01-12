from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q

from core.constants.paginator import (
    PAGE_DEFAULT,
    PAGE_SIZE_DEFAULT,
    PAGE_SIZE_MAX,
)

from .models import Tag


class TagRepository:
    def get_all_tags(self, query_params: dict | None = None):
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
            tags_qs = (
                Tag.objects.filter(query)
                .only("id", "name", "slug", "created_at", "updated_at")
            )
            paginator = Paginator(tags_qs, page_size)
            page_obj = paginator.page(page_index)
        except EmptyPage:
            return {
                "items": [],
                "total_records": 0,
                "page_index": page_index,
                "page_size": page_size,
                "total_pages": 0,
            }

        return {
            "items": page_obj.object_list,
            "total_records": paginator.count,
            "page_index": page_obj.number,
            "page_size": page_size,
            "total_pages": paginator.num_pages,
        }
    
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