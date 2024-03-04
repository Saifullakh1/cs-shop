from rest_framework.viewsets import ModelViewSet
from ..models import Clothes
from .serializers import ClothesSerializer


class ClothesAPIViewSet(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
