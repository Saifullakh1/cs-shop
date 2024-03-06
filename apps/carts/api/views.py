from rest_framework import viewsets, status, permissions
from .serializers import CartSerializer
from rest_framework.response import Response

from ..models import Cart
from apps.clothes.models import Clothes
from apps.clothes.api.serializers import ClothesSerializer


class CartAPIViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        user = request.user
        clothes = Clothes.objects.filter(cart_clothes__user_id=user)
        serializer = ClothesSerializer(clothes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



