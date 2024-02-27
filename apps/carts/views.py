from django.shortcuts import render, redirect

from .models import Cart
from apps.clothes.models import Clothes


def create(request):
    if request.method == "POST":
        clothes_id = request.POST.get('clothes_id')
        clothes = Clothes.objects.get(id=clothes_id)
        cart = Cart.objects.create(clothes_id=clothes, user_id=request.user)
        return redirect('index')

