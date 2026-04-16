import sqlite3
import os

# Đường dẫn đến db.sqlite3 (cùng thư mục với file này)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'db.sqlite3')
DATA_PATH = os.path.join(BASE_DIR, 'data.txt')


def run_import():
    """
    Đọc file data.txt và thực thi từng câu lệnh SQL vào SQLite.
    - Bỏ qua các comment (dòng bắt đầu bằng --)
    - Bỏ qua các dòng rỗng
    - Xử lý từng statement riêng lẻ để dễ debug khi lỗi
    - Dùng INSERT OR IGNORE để không báo lỗi nếu dữ liệu đã tồn tại
    """
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Khong tim thay file database: {DB_PATH}")
        return

    if not os.path.exists(DATA_PATH):
        print(f"[ERROR] Khong tim thay file du lieu: {DATA_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Tách thành từng câu lệnh SQL dựa theo dấu chấm phẩy
    statements = [s.strip() for s in raw.split(';') if s.strip()]

    success_count = 0
    error_count = 0

    for stmt in statements:
        # Bỏ qua comment thuần túy và dòng rỗng
        lines = [ln for ln in stmt.splitlines() if ln.strip() and not ln.strip().startswith('--')]
        clean_stmt = ' '.join(lines).strip()

        if not clean_stmt:
            continue

        # Chuyển INSERT INTO thành INSERT OR IGNORE INTO để tránh lỗi duplicate
        clean_stmt = clean_stmt.replace('INSERT INTO', 'INSERT OR IGNORE INTO')

        try:
            cursor.execute(clean_stmt)
            success_count += 1
        except Exception as e:
            print(f"[WARN] Loi khi thuc thi: {clean_stmt[:120]}... => {e}")
            error_count += 1

    conn.commit()
    conn.close()

    print(f"\n[OK] Hoan thanh import du lieu!")
    print(f"   Thanh cong : {success_count} cau lenh")
    print(f"   Loi        : {error_count} cau lenh")



if __name__ == '__main__':
    run_import()