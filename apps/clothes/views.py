from django.shortcuts import render
from .models import Clothes


def index(request):
    clothes = Clothes.objects.all()
    return render(request, 'clothes/clothes_list.html', {'clothes': clothes})


def clothes_detail(request, id):
    clothes = Clothes.objects.get(id=id)
    return render(request, 'clothes/clothes_detail.html', {'clothes': clothes})
