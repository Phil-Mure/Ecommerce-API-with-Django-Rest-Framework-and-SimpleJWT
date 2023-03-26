from django.db import models



CATEGORY_CHOICES = (
    ('Computers', 'Computers'),
    ('Phones', 'Phones'),
    ('Home Appliances', 'Home Appliances'),
    ('Food', 'Food')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
    
)

def get_product_image_filepath(self, filename):
	return 'product/' + str(self.product.title) + '/product_image.png'

def get_default_product_image():
	return "profile/default.png"


class Product(models.Model):
    user = models.ForeignKey('user.User',
                             on_delete=models.CASCADE, related_name='user_products', blank=True, null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(
		max_length=255, blank=True, null=True, upload_to=get_product_image_filepath, 
		default=get_default_product_image)

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    user = models.ForeignKey('user.User', related_name='ordered_products',
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"


class Order(models.Model):
    user = models.ForeignKey('user.User', related_name='orders',
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', related_name='payments', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', related_name='coupons', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return f"Order for {self.user.username}"


class Address(models.Model):
    user = models.ForeignKey('user.User', related_name='addresses',
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"Address for {self.user.username}"

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    charge_id = models.CharField(max_length=50)
    user = models.ForeignKey('user.User', related_name='user_payments',
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.user.username}"


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, related_name='refunds', on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"