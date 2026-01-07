from rest_framework.decorators import api_view
from core.error_codes import POST_SUCCESS
from core.responses import api_success

from .services import PostService
from .serializers import PostSerializer

post_service = PostService()


@api_view(["GET"])
def get_all_posts(request):
    return api_success(data=PostSerializer(post_service.get_all_posts(), many=True).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_slug(request, slug):
    return api_success(data=PostSerializer(post_service.get_post_by_slug(slug)).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_tag(request, tag_slug):
    return api_success(data=PostSerializer(post_service.get_post_by_tag(tag_slug), many=True).data, error_code=POST_SUCCESS)


@api_view(["GET"])
def get_post_by_category(request, category_slug):
    return api_success(data=PostSerializer(post_service.get_post_by_category(category_slug), many=True).data, error_code=POST_SUCCESS)
