from django.contrib import admin
from django.urls import include, path

from geo.rest_views import LocationListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/locations/', LocationListAPIView.as_view(), name='location-list'),
    path('', include('frontend.urls')),
]
