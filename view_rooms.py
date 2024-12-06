import tkinter as tk
from tkinter import ttk
from dataBase import connect_db

def view_rooms_window():
    window = tk.Toplevel()
    window.title("عرض الغرف المتاحة")
    window.geometry("500x300")

    tree = ttk.Treeview(window, columns=("room_number", "room_type", "price"), show="headings")
    tree.heading("room_number", text="رقم الغرفة")
    tree.heading("room_type", text="نوع الغرفة")
    tree.heading("price", text="السعر")
    tree.pack(fill=tk.BOTH, expand=True)

    def load_rooms():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT room_number, room_type, price FROM rooms WHERE status = 'available'")
        rows = cursor.fetchall()
        conn.close()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", tk.END, values=row)

    load_rooms()

    tk.Button(window, text="تحديث", command=load_rooms, bg="lightblue").pack(pady=10)
