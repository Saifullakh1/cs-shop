from django.shortcuts import render
from .models import Category


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})


def category_detail(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'categories/detail.html', {'category': category})
