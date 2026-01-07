from rest_framework.decorators import api_view
from core.constants.error_codes import POST_SUCCESS
from core.utils.responses import api_success

from .services import PostService
from .serializers import PostSerializer

post_service = PostService()


@api_view(["GET"])
def get_all_posts(request):
    data = post_service.get_all_posts(request.query_params)
    return api_success(data={
        "items": PostSerializer(data["items"], many=True).data,
        "totalRecords": data["total_records"],
        "totalPages": data["total_pages"],
        "pageIndex": data["page_index"],
        "pageSize": data["page_size"],
    }, error_code=POST_SUCCESS)

@api_view(["GET"])
def get_post_by_id(request, id):
    data = post_service.get_post_by_id(id)
    return api_success(data=PostSerializer(data).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_slug(request, slug):
    data = post_service.get_post_by_slug(slug)
    return api_success(data=PostSerializer(data).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_tag(request, tag_slug):
    data = post_service.get_post_by_tag(tag_slug)
    return api_success(data=PostSerializer(data, many=True).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_category(request, category_slug):
    data = post_service.get_post_by_category(category_slug)
    return api_success(data=PostSerializer(data, many=True).data, error_code=POST_SUCCESS)
