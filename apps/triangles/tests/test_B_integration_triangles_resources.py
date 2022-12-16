from typing import Dict

from django.contrib.auth import get_user_model
from django.urls import get_resolver, reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.triangles.models import Triangle


class TriangleIntegrationTestCase(APITestCase):
    def setUp(self):
        Triangle.objects.create(edge1=8, edge2=9, edge3=5)
        Triangle.objects.create(edge1=5, edge2=5, edge3=6)
        Triangle.objects.create(edge1=1, edge2=1, edge3=1)

    def create_user(self, query: Dict):
        return get_user_model().objects.create(**query)

    def get_user(self, query: Dict):
        return get_user_model().objects.get(**query)

    def get_resources(self):
        return get_resolver().reverse_dict

    def get_urls(self):
        return get_resolver().reverse_dict.keys()

    def get_urls_by_viewname(self, viewname: str):
        return reverse(viewname)

    def test_triangles_app_on_api(self):
        url = reverse("rest_register")
        response = self.client.post(
            url,
            dict(
                username="user",
                email="user@email.com",
                password1="django123",
                password2="django123",
            ),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse("token_obtain_pair")
        response = self.client.post(
            url, dict(username="user", password="django123"), format="json"
        )
        token = response.data.get("access") or response.data.get("token")
        HTTP_HEADER_AUTH = f"Bearer {token}"

        url = reverse("triangle-list")
        response = self.client.get(
            url, dict(), format="json", HTTP_AUTHORIZATION=HTTP_HEADER_AUTH
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        url = reverse("triangle-list")
        response = self.client.post(
            url,
            dict(edge1=8, edge2=9, edge3=5),
            format="json",
            HTTP_AUTHORIZATION=HTTP_HEADER_AUTH,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("type").value, "Scalene")

        url = reverse("triangle-list")
        response = self.client.get(
            url, dict(), format="json", HTTP_AUTHORIZATION=HTTP_HEADER_AUTH
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
