"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
    TokenRefreshView,
    TokenVerifyView
)
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="Game of Thrones - Django API",
        default_version='v1',
        description="A General Platform API based on Python and Django",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alves.engleandro@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/register/', include("django.contrib.auth.urls"), name="django-registration"),
    path('api/v1/accounts/', include('django.contrib.auth.urls')),
    
    path('api/v1/api-doc/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('api/v1/rest/', include('rest_framework.urls'), name="rest_framework"),
    path('api/v1/auth/', include('dj_rest_auth.urls'), name="dj-rest-auth"),
    path('api/v1/register/', include('dj_rest_auth.registration.urls'), name="dj-rest-auth-registration"), # new 
    
    path('api/v1/allauth/', include('allauth.urls'), name="allauth"),
    path('api/v1/allauth/account/', include('allauth.account.urls'), name="allauth-account"),
    path('api/v1/allauth/socialaccount/', include('allauth.socialaccount.urls'), name="allauth-socialaccount"),
    
    path('api/v1/access/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/access/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/access/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/sliding/stoken/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
    path('api/v1/sliding/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    
    path('api/v1/triangles/', include('apps.triangles.urls'), name='triangles'),
]
    