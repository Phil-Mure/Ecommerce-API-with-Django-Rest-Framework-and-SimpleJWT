from rest_framework import serializers
from . models import User 
from api.serializer import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name="user:user-detail")
    user_products = serializers.HyperlinkedRelatedField(view_name='api:product-detail', read_only=True, many=True)
    ordered_products = serializers.HyperlinkedRelatedField(view_name='api:orderproduct-detail', read_only=True, many=True) 
    orders = serializers.HyperlinkedRelatedField(view_name='api:order-detail', read_only=True, many=True)
    addresses = serializers.HyperlinkedRelatedField(view_name='api:address-detail', read_only=True, many=True)
    user_payments = serializers.HyperlinkedRelatedField(view_name='api:payment-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'id', 'url', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'user_products',
            'ordered_products', 'orders', 'addresses', 'user_payments', 
            ]