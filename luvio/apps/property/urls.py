from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

api_router = DefaultRouter()
api_router.register(r'property', PropertyViewSet, 'property')

urlpatterns = [
    url(r'/', include(api_router.urls))
]
