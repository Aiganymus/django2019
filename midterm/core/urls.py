from rest_framework.routers import DefaultRouter

from core.views import ProductViewSet, ServiceViewSet, ProductDetailViewSet, ServiceDetailViewSet

urlpatterns = []

router = DefaultRouter()
router.register('product/list', ProductViewSet, base_name='core')
router.register('product', ProductDetailViewSet, base_name='core')
router.register('service', ServiceViewSet, base_name='core')
router.register('service/list', ServiceDetailViewSet, base_name='core')

urlpatterns += router.urls
