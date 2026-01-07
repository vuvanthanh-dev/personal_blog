from .repositories import TagRepository
from core.exceptions import NotFoundException, ConflictException, ValidationException
from core.error_codes import TAG_NOT_FOUND, TAG_NAME_ALREADY_EXISTS, TAG_NAME_EMPTY


class TagService:
    def __init__(self, tag_repository: TagRepository | None = None):
        self.tag_repository = tag_repository or TagRepository()
    
    def get_all_tags(self):
        return self.tag_repository.get_all_tags()
    
    def get_tag_by_slug(self, slug: str):
        return self.tag_repository.get_tag_by_slug(slug)
    
    def create_tag(self, name: str):
        if not name.strip():
            raise ValidationException(error_code=TAG_NAME_EMPTY)
        if self.tag_repository.get_tag_by_name(name.strip()):
            raise ConflictException(error_code=TAG_NAME_ALREADY_EXISTS)
        return self.tag_repository.create_tag(name.strip())
    
    def update_tag(self, slug: str, name: str):
        if not name.strip():
            raise ValidationException(error_code=TAG_NAME_EMPTY)
        if self.tag_repository.get_tag_by_slug(slug) is None:
            raise NotFoundException(error_code=TAG_NOT_FOUND)
        return self.tag_repository.update_tag(slug, name.strip())
    
    def delete_tag(self, slug: str):
        if self.tag_repository.get_tag_by_slug(slug) is None:
            raise NotFoundException(error_code=TAG_NOT_FOUND)
        return self.tag_repository.delete_tag(slug)