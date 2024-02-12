from django.shortcuts import render
from .models import Category


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})
