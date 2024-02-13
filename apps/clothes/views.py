from django.shortcuts import render
from .models import Clothes
from apps.categories.models import Category


def index(request):
    clothes = Clothes.objects.all()
    categories = Category.objects.all()
    return render(request, 'clothes/clothes_list.html', {'clothes': clothes, 'categories': categories})


def clothes_detail(request, id):
    clothes = Clothes.objects.get(id=id)
    return render(request, 'clothes/clothes_detail.html', {'clothes': clothes})
