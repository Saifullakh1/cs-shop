from django.shortcuts import render, redirect
from .models import Clothes
from .forms import ClothesForm
from apps.categories.models import Category


def index(request):
    clothes = Clothes.objects.all()
    categories = Category.objects.all()
    return render(request, 'clothes/clothes_list.html', {'clothes': clothes, 'categories': categories})


def clothes_detail(request, id):
    clothes = Clothes.objects.get(id=id)
    return render(request, 'clothes/clothes_detail.html', {'clothes': clothes})


def create_clothes(request):
    form = ClothesForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'clothes/clothes_create.html', locals())
