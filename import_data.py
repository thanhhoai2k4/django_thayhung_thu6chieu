import sqlite3


def run_import():
    # Kết nối đến database SQLite của Django
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Đọc file data.txt và thực thi SQL
    with open('data.txt', 'r', encoding='utf-8') as file:
        sql_script = file.read()

    try:
        cursor.executescript(sql_script)
        conn.commit()
        print("Đã import dữ liệu thành công!")
    except Exception as e:
        print("Có lỗi xảy ra:", e)
    finally:
        conn.close()


if __name__ == '__main__':
    run_import()