import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'))
c = conn.cursor()

# Xoa ca ky tu \r\n that su (char 13, char 10) lan chuoi literal '\r\n' (4 ky tu)
c.execute(r"UPDATE product SET name = TRIM(REPLACE(REPLACE(REPLACE(REPLACE(name, char(13), ''), char(10), ''), '\r\n', ''), '\r', ''))")
conn.commit()

# Kiem tra lai id 3 va 4
rows = c.execute("SELECT id, name FROM product WHERE id IN (3, 4)").fetchall()
for r in rows:
    print(repr(r))

conn.close()
print("[OK] Da lam sach xong.")
