from .repositories import CategoryRepository
from core.exception.exceptions import (
    NotFoundException,
    ConflictException,
    ValidationException,
)
from core.constants.error_codes import (
    CATEGORY_NOT_FOUND,
    CATEGORY_NAME_ALREADY_EXISTS,
    CATEGORY_NAME_EMPTY,
)


class CategoryService:
    def __init__(self, category_repository: CategoryRepository | None = None):
        self.category_repository = category_repository or CategoryRepository()
    
    def get_all_categories(self, query_params: dict | None = None):
        return self.category_repository.get_all_categories(query_params)
    
    def get_category_by_slug(self, slug: str):
        return self.category_repository.get_category_by_slug(slug)
    
    def create_category(self, name: str):
        if not name.strip():
            raise ValidationException(error_code=CATEGORY_NAME_EMPTY)
        if self.category_repository.get_category_by_name(name.strip()):
            raise ConflictException(error_code=CATEGORY_NAME_ALREADY_EXISTS)
        return self.category_repository.create_category(name.strip())
    
    def update_category(self, slug: str, name: str):
        if not name.strip():
            raise ValidationException(error_code=CATEGORY_NAME_EMPTY)
        if self.category_repository.get_category_by_slug(slug) is None:
            raise NotFoundException(error_code=CATEGORY_NOT_FOUND)
        return self.category_repository.update_category(slug, name.strip())
    
    def delete_category(self, slug: str):
        if self.category_repository.get_category_by_slug(slug) is None:
            raise NotFoundException(error_code=CATEGORY_NOT_FOUND)
        return self.category_repository.delete_category(slug)