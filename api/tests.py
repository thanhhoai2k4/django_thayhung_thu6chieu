import json
from django.test import TestCase, Client
from .models import Product

class ProductApiTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_add_product(self):
        data = {
            'name': 'Test Product',
            'description': 'A nice test product',
            'price': '100000.00',
            'cate_id': 1
        }
        response = self.client.post('/api/products/add/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        resp_data = json.loads(response.content)
        self.assertEqual(resp_data['status'], 'success')
        self.assertIn('product_id', resp_data)
        
        # Verify in DB
        product = Product.objects.get(id=resp_data['product_id'])
        self.assertEqual(product.name, 'Test Product')
        
    def test_delete_product(self):
        # Create one first
        product = Product.objects.create(name='To be deleted', price=50000)
        
        response = self.client.delete(f'/api/products/{product.id}/delete/')
        self.assertEqual(response.status_code, 200)
        resp_data = json.loads(response.content)
        self.assertEqual(resp_data['status'], 'success')
        
        # Verify it's gone
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product.id)
