from django.urls import include, path
from rest_framework.routers import DefaultRouter
from trips.views import (
    TripPublicViewSet,
    ApplicationPublicViewSet,
    TripPrivateViewSet,
    ApplicationPrivateViewSet
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router_public = DefaultRouter()
router_public.register(r'trips', TripPublicViewSet, basename='public-trips')
router_public.register(r'applications', ApplicationPublicViewSet, basename='public-applications')

router_private = DefaultRouter()
router_private.register(r'trips', TripPrivateViewSet, basename='private-trips')
router_private.register(r'applications', ApplicationPrivateViewSet, basename='private-applications')

urlpatterns = [
    path('api/v1/public/', include(router_public.urls)),
    path('api/v1/private/', include(router_private.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)