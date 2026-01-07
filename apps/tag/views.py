from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from core.utils.responses import api_success
from core.constants.error_codes import TAG_SUCCESS

from .services import TagService
from .serializers import TagSerializer


tag_service = TagService()


@api_view(["GET"])
def tag_list(request):
    tags = tag_service.get_all_tags()
    return api_success(data=TagSerializer(tags, many=True).data, error_code=TAG_SUCCESS)


@api_view(["GET"])
def tag_detail(request, slug: str):
    tag = tag_service.get_tag_by_slug(slug)
    return api_success(data=TagSerializer(tag).data, error_code=TAG_SUCCESS)


@api_view(["POST"])
def create_tag(request):
    name = request.data.get("name", "")
    tag = tag_service.create_tag(name)
    return api_success(data=TagSerializer(tag).data, error_code=TAG_SUCCESS)


@api_view(["PUT"])
def update_tag(request, slug: str):
    name = request.data.get("name", "")
    tag = tag_service.update_tag(slug, name)
    return api_success(data=TagSerializer(tag).data, error_code=TAG_SUCCESS)


@api_view(["DELETE"])
def delete_tag(request, slug: str):
    tag_service.delete_tag(slug)
    return api_success(error_code=TAG_SUCCESS)
