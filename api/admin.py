from django.contrib import admin

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


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'price', 'discount_price', 'category', 'description',
        )
    search_fields = ('title',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Product, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 
        )
    search_fields = ('name',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ProductImage, ImageAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'ordered', 'product', 'quantity'
        )
    search_fields = ('product',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(OrderProduct, OrderProductAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'ref_code', 'start_date', 'ordered_date', 'ordered', 'shipping_address', 'billing_address', 
        'payment', 'coupon', 'being_delivered', 'received', 'refund_requested', 'refund_granted'
        )
    search_fields = ('ref_code',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Order, OrderAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'address_type', 'street_address', 'apartment_address', 'country', 'zip', 'address_type', 'default'
        )
    search_fields = ('address_type', 'country',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Address, AddressAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'charge_id', 'amount', 'timestamp',
        )
    search_fields = ('charge_id', 'timestamp',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Payment, PaymentAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'amount',
        )
    search_fields = ('code',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Coupon, CouponAdmin) 


class RefundAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'reason', 'accepted', 'email'
        )
    search_fields = ('email',)

    readonly_fields=('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Refund, RefundAdmin) 