from rest_framework.viewsets import ModelViewSet
from ..models import Clothes
from .serializers import ClothesSerializer
from rest_framework import permissions


class ClothesAPIViewSet(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = (permissions.IsAuthenticated, )

