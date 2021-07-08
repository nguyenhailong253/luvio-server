from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PropertyList

urlpatterns = [
    path('', PropertyList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)