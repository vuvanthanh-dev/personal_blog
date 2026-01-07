from rest_framework.decorators import api_view
from core.constants.error_codes import POST_SUCCESS
from core.utils.responses import api_success

from .services import PostService
from .serializers import PostSerializer

post_service = PostService()


@api_view(["GET"])
def get_all_posts(request):
    posts = post_service.get_all_posts(request.query_params)
    return api_success(data={
        "items": PostSerializer(posts["items"], many=True).data,
        "totalRecords": posts["total_records"],
        "totalPages": posts["total_pages"],
        "pageIndex": posts["page_index"],
        "pageSize": posts["page_size"],
    }, error_code=POST_SUCCESS)

@api_view(["GET"])
def get_post_by_id(request, id):
    post = post_service.get_post_by_id(id)
    return api_success(data=PostSerializer(post).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_slug(request, slug):
    post = post_service.get_post_by_slug(slug)
    return api_success(data=PostSerializer(post).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_tag(request, tag_slug):
    posts = post_service.get_post_by_tag(tag_slug)
    return api_success(data=PostSerializer(posts, many=True).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_category(request, category_slug):
    posts = post_service.get_post_by_category(category_slug)
    return api_success(data=PostSerializer(posts, many=True).data, error_code=POST_SUCCESS)
