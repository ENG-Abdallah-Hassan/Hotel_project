import tkinter as tk
from tkinter import messagebox
from dataBase import connect_db

def add_customer_window():
    window = tk.Toplevel()
    window.title("تسجيل عميل جديد")
    window.geometry("400x300")

    tk.Label(window, text="الاسم:", font=("Arial", 12)).pack(pady=5)
    entry_name = tk.Entry(window, font=("Arial", 12))
    entry_name.pack(pady=5)

    tk.Label(window, text="رقم الهاتف:", font=("Arial", 12)).pack(pady=5)
    entry_phone = tk.Entry(window, font=("Arial", 12))
    entry_phone.pack(pady=5)

    tk.Label(window, text="البريد الإلكتروني:", font=("Arial", 12)).pack(pady=5)
    entry_email = tk.Entry(window, font=("Arial", 12))
    entry_email.pack(pady=5)

    def save_customer():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()

        if not name or not phone or not email:
            messagebox.showwarning("تحذير", "يرجى إدخال جميع الحقول!")
        else:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO customers (name, phone, email)
            VALUES (?, ?, ?)
            """, (name, phone, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("نجاح", "تم إضافة العميل بنجاح!")
            entry_name.delete(0, tk.END)
            entry_phone.delete(0, tk.END)
            entry_email.delete(0, tk.END)

    tk.Button(window, text="إضافة العميل", command=save_customer, bg="lightblue", font=("Arial", 12)).pack(pady=20)
