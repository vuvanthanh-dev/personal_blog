from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .services import TagService
from .serializers import TagSerializer


tag_service = TagService()


@api_view(["GET"])
def tag_list(request):
    tags = tag_service.get_all_tags()
    return Response(
        TagSerializer(tags, many=True).data,
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
def tag_detail(request, slug: str):
    tag = tag_service.get_tag_by_slug(slug)
    if not tag:
        return Response({"detail": "Tag not found."}, status=404)
    return Response(TagSerializer(tag).data)


@api_view(["POST"])
def create_tag(request):
    name = request.data.get("name", "").strip()
    if not name:
        return Response({"detail": "Tag name cannot be empty."}, status=400)
    
    tag = tag_service.create_tag(name)
    return Response(TagSerializer(tag).data)


@api_view(["PUT"])
def update_tag(request, slug: str):
    name = request.data.get("name", "").strip()
    if not name:
        return Response({"detail": "Tag name cannot be empty."}, status=400)
    
    tag = tag_service.update_tag(slug, name)
    return Response(TagSerializer(tag).data)


@api_view(["DELETE"])
def delete_tag(request, slug: str):
    if tag_service.delete_tag(slug):
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({"detail": "Tag not found."}, status=404)
