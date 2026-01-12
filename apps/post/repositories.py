from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q

from core.constants.paginator import (
    PAGE_DEFAULT,
    PAGE_SIZE_DEFAULT,
    PAGE_SIZE_MAX,
)
from .models import Post

class PostRepository:
    def get_all_posts(self, query_params: dict | None = None):
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
        title = (
            query_params.get("title", "")
            if query_params
            else ""
        )
        category = (
            query_params.get("category", "")
            if query_params
            else ""
        )
        tag = (
            query_params.get("tag", "")
            if query_params
            else ""
        )

        if page_size > PAGE_SIZE_MAX:
            page_size = PAGE_SIZE_MAX

        query = Q()

        if title:
            query &= Q(title__icontains=title)

        if category:
            query &= Q(categories__slug=category)

        if tag:
            query &= Q(tags__slug=tag)

        try:
            posts_qs = (
                Post.objects.filter(query)
                .only("id", "title", "slug", "created_at", "updated_at")
                .prefetch_related("categories", "tags")
            )
            paginator = Paginator(posts_qs, page_size)
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

    def get_post_by_id(self, id: int) -> Post | None:
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return None
    
    def get_post_by_slug(self, slug: str) -> Post | None:
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return None
    
    def get_post_by_title(self, title: str) -> Post | None:
        try:
            return Post.objects.get(title=title)
        except Post.DoesNotExist:
            return None

    def get_post_by_tag(self, tag_slug: str):
        return Post.objects.filter(tags__slug=tag_slug)

    def get_post_by_category(self, category_slug: str):
        return Post.objects.filter(categories__slug=category_slug)
    
    def create_post(self, title: str, content: str, categories: list[str], tags: list[str]) -> Post | None:
        try:
            return Post.objects.create(title=title, content=content, categories=categories, tags=tags)
        except Post.DoesNotExist:
            return None
    
    def update_post(self, slug: str, title: str, content: str, categories: list[str], tags: list[str]) -> Post | None:
        post = self.get_post_by_slug(slug)
        if post:
            post.title = title
            post.content = content
            post.categories = categories
            post.tags = tags
            post.save()
            return post
        return None
    
    def delete_post(self, slug: str) -> bool:
        post = self.get_post_by_slug(slug)
        if post:
            post.is_active = False
            post.save()
            return True
        return False