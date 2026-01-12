from .repositories import TagRepository
from core.exception.exceptions import (
    NotFoundException,
    ConflictException,
    ValidationException
)
from core.constants.error_codes import (
    TAG_NOT_FOUND,
    TAG_NAME_ALREADY_EXISTS,
    TAG_NAME_EMPTY
)
from apps.tag.models import Tag

class TagService:
    def __init__(self, tag_repository: TagRepository | None = None):
        self.tag_repository = tag_repository or TagRepository()
    
    def get_all_tags(self, query_params: dict | None = None):
        return self.tag_repository.get_all_tags(query_params)
    
    def get_tag_by_slug(self, slug: str) -> Tag:
        return self.tag_repository.get_tag_by_slug(slug)
    
    def create_tag(self, name: str) -> Tag:
        if not name.strip():
            raise ValidationException(error_code=TAG_NAME_EMPTY)
        if self.tag_repository.get_tag_by_name(name.strip()):
            raise ConflictException(error_code=TAG_NAME_ALREADY_EXISTS)
        return self.tag_repository.create_tag(name.strip())
    
    def update_tag(self, slug: str, name: str) -> Tag:
        if not name.strip():
            raise ValidationException(error_code=TAG_NAME_EMPTY)
        if self.tag_repository.get_tag_by_slug(slug) is None:
            raise NotFoundException(error_code=TAG_NOT_FOUND)
        return self.tag_repository.update_tag(slug, name.strip())
    
    def delete_tag(self, slug: str) -> None:
        if self.tag_repository.get_tag_by_slug(slug) is None:
            raise NotFoundException(error_code=TAG_NOT_FOUND)
        return self.tag_repository.delete_tag(slug)