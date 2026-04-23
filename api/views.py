from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, ProductImage, ProductStock


def home(request):
    return JsonResponse({'message': 'Welcome to the Product API!'})


# ─── API 1: Lấy danh sách tất cả sản phẩm ────────────────────────────────────
def get_products(request):
    """GET /api/products/ - Trả về toàn bộ sản phẩm"""
    products = list(Product.objects.all().values())
    return JsonResponse({'status': 'success', 'count': len(products), 'data': products}, safe=False)


# ─── API 2: Tìm sản phẩm theo ID ─────────────────────────────────────────────
def get_product_by_id(request, product_id):
    """GET /api/products/<product_id>/ - Trả về sản phẩm theo ID"""
    product = get_object_or_404(Product, id=product_id)
    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': str(product.price),
        'cate_id': product.cate_id,
        'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S') if product.created_at else None,
    }
    return JsonResponse({'status': 'success', 'data': data})


# ─── API 3: Lấy ảnh sản phẩm theo ID ────────────────────────────────────────
def get_image_by_id(request, image_id):
    """GET /api/images/<image_id>/ - Trả về thông tin ảnh sản phẩm theo ID"""
    image = get_object_or_404(ProductImage, id=image_id)
    data = {
        'id': image.id,
        'product_id': image.product_id,
        'path': image.path,
        'is_main': image.is_main,
    }
    return JsonResponse({'status': 'success', 'data': data})


# ─── API 4: Tìm kiếm sản phẩm theo tên ──────────────────────────────────────
def get_item_by_name(request):
    """GET /api/products/search/?name=<keyword> - Tìm sản phẩm theo tên (gần đúng)"""
    keyword = request.GET.get('name', '').strip()

    if not keyword:
        return JsonResponse(
            {'status': 'error', 'message': 'Thieu tham so "name". Vi du: /api/products/search/?name=TEE'},
            status=400
        )

    products = Product.objects.filter(name__icontains=keyword).values()
    result = list(products)

    return JsonResponse({
        'status': 'success',
        'keyword': keyword,
        'count': len(result),
        'data': result,
    })


# ─── API 5: Lấy danh sách theo product_id và size_id ────────────────────────
def get_stock_by_product_and_size(request):
    """GET /api/stock/search/?product_id=<id>&size_id=<id> - Lấy danh sách theo size và product id"""
    product_id = request.GET.get('product_id')
    size_id = request.GET.get('size_id')

    if not product_id or not size_id:
        return JsonResponse(
            {'status': 'error', 'message': 'Thieu tham so "product_id" hoac "size_id". VD: /api/stock/search/?product_id=1&size_id=2'},
            status=400
        )

    try:
        product_id = int(product_id)
        size_id = int(size_id)
    except ValueError:
        return JsonResponse(
            {'status': 'error', 'message': 'Tham so "product_id" va "size_id" phai la so nguyen.'},
            status=400
        )

    stocks = ProductStock.objects.filter(product_id=product_id, size_id=size_id).values()
    result = list(stocks)

    return JsonResponse({
        'status': 'success',
        'product_id': product_id,
        'size_id': size_id,
        'count': len(result),
        'data': result,
    })
