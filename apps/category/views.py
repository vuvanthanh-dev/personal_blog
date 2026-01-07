
from rest_framework.decorators import api_view
from core.constants.error_codes import CATEGORY_SUCCESS
from core.utils.responses import api_success

from .services import CategoryService
from .serializers import CategorySerializer


category_service = CategoryService()


@api_view(["GET"])
def get_all_categories(request):
    return api_success(data=CategorySerializer(category_service.get_all_categories(), many=True).data, error_code=CATEGORY_SUCCESS)


@api_view(["GET"])
def get_category_by_slug(request, slug):
    return api_success(data=CategorySerializer(category_service.get_category_by_slug(slug)).data, error_code=CATEGORY_SUCCESS)