import os
import sys

# 1. Thêm đường dẫn của thư mục gốc dự án vào hệ thống
# Giúp hệ thống tìm thấy thư mục 'thanhhoai' và các thư viện liên quan
sys.path.insert(0, os.path.dirname(__file__))

# 2. Khai báo file settings của project
# Trong mã nguồn của bạn, project chính tên là "thanhhoai"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thanhhoai.settings')

# 3. Nạp application từ Django để cPanel có thể khởi chạy web
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()