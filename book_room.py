import tkinter as tk
from tkinter import messagebox
from dataBase import connect_db

def book_room_window():
    window = tk.Toplevel()
    window.title("حجز غرفة")
    window.geometry("400x300")

    # مدخلات البيانات
    tk.Label(window, text="رقم العميل:", font=("Arial", 12)).pack(pady=5)
    entry_customer_id = tk.Entry(window, font=("Arial", 12))
    entry_customer_id.pack(pady=5)

    tk.Label(window, text="رقم الغرفة:", font=("Arial", 12)).pack(pady=5)
    entry_room_number = tk.Entry(window, font=("Arial", 12))
    entry_room_number.pack(pady=5)

    tk.Label(window, text="تاريخ الدخول:", font=("Arial", 12)).pack(pady=5)
    entry_check_in = tk.Entry(window, font=("Arial", 12))
    entry_check_in.pack(pady=5)

    tk.Label(window, text="تاريخ الخروج:", font=("Arial", 12)).pack(pady=5)
    entry_check_out = tk.Entry(window, font=("Arial", 12))
    entry_check_out.pack(pady=5)

    def book_room():
        customer_id = entry_customer_id.get()
        room_number = entry_room_number.get()
        check_in = entry_check_in.get()
        check_out = entry_check_out.get()

        if not customer_id or not room_number or not check_in or not check_out:
            messagebox.showwarning("تحذير", "يرجى إدخال جميع الحقول!")
        else:
            conn = connect_db()
            cursor = conn.cursor()

            # تحقق إذا كانت الغرفة متاحة
            cursor.execute("SELECT status FROM rooms WHERE room_number = ? AND status = 'available'", (room_number,))
            room = cursor.fetchone()

            if room:
                cursor.execute("""
                INSERT INTO bookings (customer_id, room_number, check_in, check_out)
                VALUES (?, ?, ?, ?)
                """, (customer_id, room_number, check_in, check_out))

                cursor.execute("UPDATE rooms SET status = 'booked' WHERE room_number = ?", (room_number,))
                conn.commit()
                conn.close()
                messagebox.showinfo("نجاح", "تم الحجز بنجاح!")
            else:
                messagebox.showwarning("تحذير", "الغرفة غير متاحة!")

    tk.Button(window, text="حجز الغرفة", command=book_room, bg="lightblue", font=("Arial", 12)).pack(pady=20)
