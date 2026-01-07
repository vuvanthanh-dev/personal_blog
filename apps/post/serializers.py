from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "content", "created_at", "updated_at", "categories", "tags"]