from rest_framework import routers
from .views import (
    ProductViewSet, ImageViewSet, OrderedProductViewSet, OrderViewSet, AddressViewSet, PaymentViewSet,
    CouponViewSet, RefundViewSet
    )
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product_images', ImageViewSet)
router.register(r'ordered_products', OrderedProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'refunds', RefundViewSet)

app_name='api'
urlpatterns = [
    path('api/', include((router.urls))),
]