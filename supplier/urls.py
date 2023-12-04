from rest_framework.routers import DefaultRouter
from supplier.apps import SupplierConfig
from supplier.views import *


app_name = SupplierConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [

        ] + router.urls
