import sqlite3

DB_NAME = "hotel.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()

    # إنشاء جدول الغرف
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rooms (
        room_number INTEGER PRIMARY KEY,
        room_type TEXT NOT NULL,
        price REAL NOT NULL,
        status TEXT DEFAULT 'available'
    )
    """)

    # إنشاء جدول العملاء
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    # إنشاء جدول الحجوزات
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        room_number INTEGER,
        check_in TEXT NOT NULL,
        check_out TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (room_number) REFERENCES rooms(room_number)
    )
    """)

    # إنشاء جدول الفواتير
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_id INTEGER,
        total_amount REAL,
        FOREIGN KEY (booking_id) REFERENCES bookings(id)
    )
    """)

    conn.commit()
    conn.close()

# اختبار الاتصال وإنشاء الجداول
if __name__ == "__main__":
    initialize_db()
    print("تم تهيئة قاعدة البيانات!")
