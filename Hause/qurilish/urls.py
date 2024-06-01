from django.urls import path, include
from . views import RegionViewSet, OrganizationViewSet, BuildingViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



router = routers.DefaultRouter()
router.register('region-list', RegionViewSet)
router.register('org-list', OrganizationViewSet)
router.register('buil-list', BuildingViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('region_list', include(router.urls)),
    path('org_list', include(router.urls)),
    path('buil_list', include(router.urls)),
]
