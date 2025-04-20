from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planets.views import PlanetViewSet

router = DefaultRouter()
router.register(r'planets', PlanetViewSet, basename='planet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]