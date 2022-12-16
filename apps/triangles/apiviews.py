import logging

from environs import Env
from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.triangles.models import Triangle
from apps.triangles.serializers import TriangleSerializer

env = Env()
env.read_env()

logger = logging.getLogger(env.str("AWS_CLOUDWATCH_LOGGER"))


class UserSecThrottle(UserRateThrottle):
    scope = "user_sec"


class TrianglesViewSet(viewsets.ModelViewSet):
    """
    Triangle App on API. It provides a triangle classification
    based on the lengths of its three sides.\n
    NOTE:
    * At browser, find out more about the API at /api/v1/doc/
    * You need to be authenticated to use this API.
    * You can create a triangle by sending a POST request
    * You can get the last created triangles by sending a GET request
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JWTAuthentication,
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    queryset = Triangle.objects.all().order_by("-created_at")
    serializer_class = TriangleSerializer
    throttle_classes = [UserSecThrottle]
