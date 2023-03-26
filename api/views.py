from django.shortcuts import render
from rest_framework import viewsets
from .serializer import (
    ProductSerializer, ImageSerializer, OrderProductSerializer, OrderSerializer, AddressSerializer,
    PaymentSerializer, CouponSerializer, RefundSerializer
    )
from rest_framework import permissions
from .permissions import IsUserOrReadOnly
from .models import Product, ProductImage, OrderProduct, Order, Address, Payment, Coupon, Refund 


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('product_images')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.select_related('product')
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderedProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.select_related('product')  
    serializer_class = OrderProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related(
        'shipping_address', 'billing_address', 'payment', 'coupon'
        ).prefetch_related('products', 'refunds')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]