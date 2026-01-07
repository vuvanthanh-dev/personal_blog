from django.utils.text import slugify

from .models import Post


class PostRepository:
    def get_all_posts(self):
        return Post.objects.filter(is_active=True).order_by("-created_at")
    
    def get_post_by_slug(self, slug: str) -> Post | None:
        try:
            return Post.objects.get(slug=slug, is_active=True)
        except Post.DoesNotExist:
            return None
    
    def get_post_by_title(self, title: str) -> Post | None:
        try:
            return Post.objects.get(title=title, is_active=True)
        except Post.DoesNotExist:
            return None
    
    def create_post(self, title: str, content: str) -> Post | None:
        try:
            return Post.objects.create(title=title, content=content)
        except Post.DoesNotExist:
            return None
    
    def update_post(self, slug: str, title: str, content: str) -> Post | None:
        post = self.get_post_by_slug(slug)
        if post:
            post.title = title
            post.content = content
            post.slug = slugify(title)
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