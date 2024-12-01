from rest_framework.routers import DefaultRouter
from .views_v2 import PostViewSetV2

router = DefaultRouter()
router.register(r'posts', PostViewSetV2)

urlpatterns = router.urls
    