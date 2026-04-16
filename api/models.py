from django.db import models


# ─── Danh mục sản phẩm ────────────────────────────────────────────────────────
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


# ─── Sản phẩm ─────────────────────────────────────────────────────────────────
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cate_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


# ─── Ảnh sản phẩm ─────────────────────────────────────────────────────────────
class ProductImage(models.Model):
    product_id = models.IntegerField(null=True, blank=True)
    path = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_image'

    def __str__(self):
        return self.path


# ─── Kích thước ───────────────────────────────────────────────────────────────
class Size(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'size'

    def __str__(self):
        return self.name


# ─── Tồn kho sản phẩm ─────────────────────────────────────────────────────────
class ProductStock(models.Model):
    product_id = models.IntegerField(null=True, blank=True)
    size_id = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'product_stock'

    def __str__(self):
        return f"Stock product_id={self.product_id} size_id={self.size_id}"


# ─── Đơn hàng ─────────────────────────────────────────────────────────────────
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipping', 'Shipping'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    ]
    user_id = models.IntegerField(null=True, blank=True)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Order #{self.id} - {self.fullname}"


# ─── Chi tiết đơn hàng ────────────────────────────────────────────────────────
class OrderItem(models.Model):
    order_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    size_id = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return f"OrderItem order_id={self.order_id} product_id={self.product_id}"


# ─── Giỏ hàng ─────────────────────────────────────────────────────────────────
class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    size_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"Cart user_id={self.user_id} product_id={self.product_id}"