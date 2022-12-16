from rest_framework.routers import SimpleRouter

from apps.triangles.apiviews import TrianglesViewSet

app = "triangles"

router = SimpleRouter()

router.register(r"", TrianglesViewSet)

urlpatterns = []
urlpatterns += router.urls
