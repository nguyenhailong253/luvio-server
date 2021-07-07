from rest_framework import mixins, permissions, serializers
from rest_framework.viewsets import GenericViewSet

# Create your views here.
class PropertyViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """[summary]

    Args:
        mixins ([type]): [description]
        mixins ([type]): [description]
        GenericViewSet ([type]): [description]
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()