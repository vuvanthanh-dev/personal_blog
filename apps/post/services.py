from core.exception.exceptions import NotFoundException, ValidationException
from core.utils.hash_id import decode_id
from core.constants.error_codes import (
    POST_ID_EMPTY,
    POST_TITLE_EMPTY,
    POST_CONTENT_EMPTY,
    POST_NOT_FOUND,
    POST_TITLE_ALREADY_EXISTS,
    POST_TAG_EMPTY,
    POST_CATEGORY_EMPTY,
)
from .repositories import PostRepository

class PostService:
    def __init__(self, post_repository: PostRepository | None = None):
        self.post_repository = post_repository or PostRepository()

    def get_post_by_id(self, hash_id: str):
        if not hash_id.strip():
            raise ValidationException(error_code=POST_ID_EMPTY)
        id = decode_id(hash_id.strip())
        if id is None:
            raise NotFoundException(error_code=POST_NOT_FOUND)
        return self.post_repository.get_post_by_id(id)
    
    def get_all_posts(self, query_params: dict | None = None):
        return self.post_repository.get_all_posts(query_params)
    
    def get_post_by_slug(self, slug: str):
        return self.post_repository.get_post_by_slug(slug)

    def get_post_by_tag(self, tag_slug: str):
        if not tag_slug.strip():
            raise ValidationException(error_code=POST_TAG_EMPTY)
        return self.post_repository.get_post_by_tag(tag_slug.strip())

    def get_post_by_category(self, category_slug: str):
        if not category_slug.strip():
            raise ValidationException(error_code=POST_CATEGORY_EMPTY)
        return self.post_repository.get_post_by_category(category_slug.strip())
    
    def create_post(self, title: str, content: str, categories: list[str], tags: list[str]):
        if not title.strip():
            raise ValidationException(error_code=POST_TITLE_EMPTY)
        if not content.strip():
            raise ValidationException(error_code=POST_CONTENT_EMPTY)
        if self.post_repository.get_post_by_title(title.strip()):
            raise ValidationException(error_code=POST_TITLE_ALREADY_EXISTS)
        return self.post_repository.create_post(title, content)
    
    def update_post(self, slug: str, title: str, content: str, categories: list[str], tags: list[str]):
        if not title.strip():
            raise ValidationException(error_code=POST_TITLE_EMPTY)
        if not content.strip():
            raise ValidationException(error_code=POST_CONTENT_EMPTY)
        if self.post_repository.get_post_by_slug(slug) is None:
            raise NotFoundException(error_code=POST_NOT_FOUND)
        return self.post_repository.update_post(slug, title, content, categories, tags)
    
    def delete_post(self, slug: str):
        if self.post_repository.get_post_by_slug(slug) is None:
            raise NotFoundException(error_code=POST_NOT_FOUND)
        return self.post_repository.delete_post(slug)
