from rest_framework import serializers


from .models import (
    Product,
    ProductImage,
    OrderProduct,
    Order,
    Address,
    Payment,
    Coupon,
    Refund
)

        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="api:product-detail")
    product_images = serializers.HyperlinkedRelatedField(
        view_name="api:productimage-detail", read_only=True, many=True
        )    

    class Meta:
        model = Product
        fields = [
            'id', 'url', 'user', 'title', 'price', 'discount_price', 'category', 'description', 'product_images'
            ]


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:productimage-detail")  
    product = serializers.HyperlinkedRelatedField(
        view_name="api:product-detail", read_only=False, queryset = Product.objects.prefetch_related('product_images'),
        )  

    class Meta:
        model = ProductImage
        fields = ('id', 'name', 'url', 'image', 'product') 


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="api:orderproduct-detail")
    product = serializers.HyperlinkedRelatedField(
        view_name="api:product-detail", queryset = Product.objects.prefetch_related('product_images')
        )  

    class Meta:
        model = OrderProduct
        fields = ['id', 'user', 'url', 'ordered', 'product', 'quantity'] 


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="api:order-detail")
    products = serializers.HyperlinkedRelatedField(
        view_name="api:orderproduct-detail", read_only=False, queryset = OrderProduct.objects.all(), many=True
        ) 
    shipping_address = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail", read_only=False, queryset = Address.objects.all()
        ) 
    billing_address = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail", read_only=False, queryset = Address.objects.all()
        ) 
    payment = serializers.HyperlinkedRelatedField(
        view_name="api:payment-detail", read_only=False, queryset = Payment.objects.all()
        ) 
    coupon = serializers.HyperlinkedRelatedField(
        view_name="api:coupon-detail", read_only=False, queryset = Coupon.objects.all() 
        ) 
    refunds = serializers.HyperlinkedRelatedField(
        view_name="api:refund-detail", read_only=False, queryset = Refund.objects.prefetch_related('order'), many=True
        ) 


    class Meta:
        model = Order
        fields = [
            'id', 'user', 'ref_code', 'url', 'products', 'start_date', 'ordered_date', 'ordered', 'shipping_address',
            'billing_address', 'payment', 'coupon', 'being_delivered', 'received', 'refunds', 'refund_requested', 
            'refund_granted',
                  ] 
        

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="api:address-detail") 

    class Meta:
        model = Address
        fields = [
            'id', 'url', 'user', 'street_address', 'apartment_address', 'country', 'zip', 'address_type', 'default'
            ]

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="api:payment-detail") 

    class Meta:
        model = Payment
        fields = [
            'id', 'url', 'user', 'charge_id', 'amount', 'timestamp', 
            ]

class CouponSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:coupon-detail") 

    class Meta:
        model = Coupon
        fields = [
            'id', 'url', 'code', 'amount', 
            ]


class RefundSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="api:refund-detail") 
    order = serializers.HyperlinkedRelatedField(
        view_name="api:order-detail", read_only=False, queryset = Order.objects.select_related(
        'shipping_address', 'billing_address', 'payment', 'coupon'
        ).prefetch_related('products', 'refunds')
        )

    class Meta:
        model = Refund
        fields = [
            'id', 'url', 'user', 'order', 'reason', 'accepted', 'email' 
            ]