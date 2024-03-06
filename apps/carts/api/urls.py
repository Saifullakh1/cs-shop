from rest_framework import routers
from .views import CartAPIViewSet

router = routers.DefaultRouter()
router.register(
    "carts",
    CartAPIViewSet
)

urlpatterns = router.urls