from rest_framework.serializers import ModelSerializer

from apps.triangles.models import Triangle


class TriangleSerializer(ModelSerializer):
    class Meta:
        model = Triangle
        fields = ["edge1", "edge2", "edge3", "type"]
