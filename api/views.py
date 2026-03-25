from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product


# API 1: Lấy danh sách tất cả sản phẩm
def get_products(request):
    # Lấy toàn bộ sản phẩm và chuyển thành dạng dictionary
    products = list(Product.objects.all().values())
    return JsonResponse({'status': 'success', 'data': products}, safe=False)


# API 2: Tìm sản phẩm dựa trên ID
def get_product_by_id(request, product_id):
    # Tìm sản phẩm theo ID, nếu không có sẽ trả về lỗi 404
    product = get_object_or_404(Product, id=product_id)

    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': str(product.price),  # Convert Decimal sang string để serialize JSON
        'cate_id': product.cate_id,
        'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    }

    return JsonResponse({'status': 'success', 'data': data})