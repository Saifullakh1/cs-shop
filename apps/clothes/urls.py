from django.urls.conf import path
from .views import index, clothes_detail, create_clothes


urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', clothes_detail, name='clothes-detail'),
    path('create/', create_clothes, name='create-clothes')
]
