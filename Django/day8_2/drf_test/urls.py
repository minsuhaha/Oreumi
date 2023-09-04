from rest_framework.routers import DefaultRouter
from .views import TODOViewSet

# router는 네트워크 패킷의 방향을 정해주는 것
router = DefaultRouter()
router.register('drf_test', TODOViewSet)

urlpatterns = router.urls
