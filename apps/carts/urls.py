from django.urls import path
from .views import create

urlpatterns = [
    path('cart', create, name='cart-create')
]
