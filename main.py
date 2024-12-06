import tkinter as tk
from add_customer import add_customer_window
from view_rooms import view_rooms_window
from book_room import book_room_window
from checkout import checkout_window 

def main():
    root = tk.Tk()
    root.title("نظام إدارة الفندق")
    root.geometry("300x400")

    tk.Button(root, text="إضافة عميل جديد", command=add_customer_window, bg="lightgreen", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="عرض الغرف المتاحة", command=view_rooms_window, bg="lightblue", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="حجز غرفة", command=book_room_window, bg="lightyellow", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="تسجيل الخروج وحساب الفاتورة", command=checkout_window, bg="lightpink", font=("Arial", 14)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
