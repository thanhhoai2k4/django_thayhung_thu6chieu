from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # API 1: Lấy toàn bộ sản phẩm
    path('products/', views.get_products, name='get_products'),

    # API 2: Lấy sản phẩm theo ID
    path('products/<int:product_id>/', views.get_product_by_id, name='get_product_by_id'),

    # API 3: Lấy ảnh sản phẩm theo ID  →  GET /api/images/<image_id>/
    path('images/<int:image_id>/', views.get_image_by_id, name='get_image_by_id'),

    # API 4: Tìm sản phẩm theo tên     →  GET /api/products/search/?name=keyword
    path('products/search/', views.get_item_by_name, name='get_item_by_name'),

    # API 5: Tìm theo product_id và size_id  →  GET /api/stock/search/?product_id=1&size_id=2
    path('stock/search/', views.get_stock_by_product_and_size, name='get_stock_by_product_and_size'),
]
