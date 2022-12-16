from rest_framework.test import APITestCase

from apps.triangles.models import Triangle


class TriangleUnitTestCase(APITestCase):
    def setUp(self):
        Triangle.objects.create(edge1=8, edge2=9, edge3=5)
        Triangle.objects.create(edge1=5, edge2=5, edge3=6)
        Triangle.objects.create(edge1=1, edge2=1, edge3=1)

    def create_scalene_triangle(self):
        return Triangle.objects.create(edge1=8, edge2=9, edge3=5)

    def create_isosceles_triangle(self):
        return Triangle.objects.create(edge1=5, edge2=5, edge3=6)

    def create_equilateral_triangle(self):
        return Triangle.objects.create(edge1=1, edge2=1, edge3=1)

    def test_to_get_type_from_triangle(self):
        triangle = Triangle.objects.get(pk=1)
        self.assertEqual(triangle.type(), "Scalene")

        triangle = Triangle.objects.get(pk=2)
        self.assertEqual(triangle.type(), "Isosceles")

        triangle = Triangle.objects.get(pk=3)
        self.assertEqual(triangle.type(), "Equilateral")
