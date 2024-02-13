from django.urls import path
from .views import categories, category_detail

urlpatterns = [
    path('categories', categories, name='category-list'),
    path('category/<int:id>', category_detail, name='category-detail')
]
