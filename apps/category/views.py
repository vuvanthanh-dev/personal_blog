
from rest_framework.decorators import api_view
from core.constants.error_codes import CATEGORY_SUCCESS
from core.utils.responses import api_success

from .services import CategoryService
from .serializers import CategorySerializer


category_service = CategoryService()


@api_view(["GET"])
def get_all_categories(request):
    categories = category_service.get_all_categories(request.query_params)
    return api_success(data={
        "items": CategorySerializer(categories["items"], many=True).data,
        "totalRecords": categories["total_records"],
        "totalPages": categories["total_pages"],
        "pageIndex": categories["page_index"],
        "pageSize": categories["page_size"],
    }, error_code=CATEGORY_SUCCESS)


@api_view(["GET"])
def get_category_by_slug(request, slug):
    category = category_service.get_category_by_slug(slug)
    return api_success(data=CategorySerializer(category).data, error_code=CATEGORY_SUCCESS)