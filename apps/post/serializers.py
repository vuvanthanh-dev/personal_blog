from rest_framework import serializers

from core.utils.hash_id import encode_id
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")
    id = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "categories",
            "tags",
            "created_at",
            "updated_at",
        ]

    def get_id(self, obj):
        return encode_id(obj.id)