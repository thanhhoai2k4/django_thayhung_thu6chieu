from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cate_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        # Cấu hình db_table để Django tạo bảng với tên chính xác là 'product'
        # (thay vì mặc định là 'api_product'), giúp câu lệnh SQL trong data.txt chạy đúng.
        db_table = 'product'

    def __str__(self):
        return self.name