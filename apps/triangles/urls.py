from rest_framework.routers import SimpleRouter

#from apps.triangles.apiviews import HouseViewSet, MemberViewSet

app = 'triangles'

router = SimpleRouter()

#router.register(r'houses', HouseViewSet)
#router.register(r'members', MemberViewSet)

urlpatterns = []
urlpatterns += router.urls
