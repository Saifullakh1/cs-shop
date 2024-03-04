from rest_framework import routers
from .views import ClothesAPIViewSet

router = routers.DefaultRouter()

router.register(
    "clothes",
    ClothesAPIViewSet
)

urlpatterns = router.urls
