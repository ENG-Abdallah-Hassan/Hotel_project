import tkinter as tk
from tkinter import messagebox
from dataBase import connect_db 
from datetime import datetime

def checkout_window():
    window = tk.Toplevel()
    window.title("تسجيل الخروج وحساب الفاتورة")
    window.geometry("400x300")

    tk.Label(window, text="رقم الحجز:", font=("Arial", 12)).pack(pady=5)
    entry_booking_id = tk.Entry(window, font=("Arial", 12))
    entry_booking_id.pack(pady=5)

    def checkout():
        booking_id = entry_booking_id.get()

        if not booking_id:
            messagebox.showwarning("تحذير", "يرجى إدخال رقم الحجز!")
        else:
            conn = connect_db()
            cursor = conn.cursor()

            # استرجاع تفاصيل الحجز
            cursor.execute("""
            SELECT bookings.id, rooms.room_number, rooms.price, bookings.check_in, bookings.check_out
            FROM bookings
            JOIN rooms ON bookings.room_number = rooms.room_number
            WHERE bookings.id = ?
            """, (booking_id,))
            booking = cursor.fetchone()

            if booking:
                room_number, price, check_in, check_out = booking
                check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

                # حساب عدد الأيام
                days_stayed = (check_out_date - check_in_date).days

                if days_stayed <= 0:
                    messagebox.showwarning("تحذير", "تاريخ الخروج غير صحيح!")
                else:
                    total_amount = price * days_stayed

                    # إضافة الفاتورة إلى قاعدة البيانات
                    cursor.execute("""
                    INSERT INTO invoices (booking_id, total_amount)
                    VALUES (?, ?)
                    """, (booking_id, total_amount))

                    # تحديث حالة الغرفة إلى "متاحة"
                    cursor.execute("UPDATE rooms SET status = 'available' WHERE room_number = ?", (room_number,))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("فاتورة", f"إجمالي الفاتورة: {total_amount} جنيه")
            else:
                messagebox.showwarning("خطأ", "رقم الحجز غير موجود!")

    tk.Button(window, text="تسجيل الخروج وحساب الفاتورة", command=checkout, bg="lightblue", font=("Arial", 12)).pack(pady=20)
