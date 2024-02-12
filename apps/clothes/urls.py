from django.urls.conf import path
from .views import index, clothes_detail


urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', clothes_detail, name='clothes-detail')
]
