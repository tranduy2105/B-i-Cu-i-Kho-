import json
import tkinter as tk
from tkinter import ttk

DATA_FILE = "data_tai_khoan.json"

def read_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as myfile:
            return json.load(myfile)
    except:
        return []

def clear_tree_view(mytree):
    for item in mytree.get_children():
        mytree.delete(item)

def load_account_data(mytreeview, data=None):
    clear_tree_view(mytreeview)
    if data is None:
        data = read_data()        
    for item in data:
        mytreeview.insert(parent='', index='end', values=(
            item['ten_app'], item['ten_dang_nhap'], item['mat_khau'], item['chu_tk'], item['tinh_trang']
        ))

def add_account():
    new_account = {
        "ten_app": tenapp.get(),
        "ten_dang_nhap": tendnh.get(),
        "mat_khau": matkhau.get(),
        "chu_tk": chutk.get(),
        "tinh_trang": tinhtrang.get()
    }
    data = read_data()
    data.append(new_account)
    load_account_data(tree, data)

root = tk.Tk()
root.title("Quản lý tài khoản")
root.geometry("1000x400")

# Frames
list_hh_frame = ttk.Frame(root)
list_button_frame = ttk.Frame(root)
input_hh_frame = ttk.Frame(root)
list_hh_frame.grid(row=0, column=0)
list_button_frame.grid(row=1, column=0)
input_hh_frame.grid(row=2, column=0)

# Treeview
columns = ('ten_app', 'ten_dang_nhap', 'mat_khau', 'chu_tk', 'tinh_trang')
tree = ttk.Treeview(list_hh_frame, columns=columns, show='headings')
tree.heading('ten_app', text='Tên App')
tree.heading('ten_dang_nhap', text='Tên Đăng Nhập')
tree.heading('mat_khau', text='Mật Khẩu')
tree.heading('chu_tk', text='Chủ Tài Khoản')
tree.heading('tinh_trang', text='Tình Trạng')
tree.pack()

# Buttons
ttk.Button(list_button_frame, text="Xóa danh sách", command=lambda: clear_tree_view(tree)).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(list_button_frame, text="Lấy danh sách", command=lambda: load_account_data(tree)).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(list_button_frame, text="Thêm", command=add_account).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(list_button_frame, text="Xóa").grid(row=0, column=3, padx=5, pady=5)
ttk.Button(list_button_frame, text="Cập nhật").grid(row=0, column=4, padx=5, pady=5)

# Input Fields
ttk.Label(input_hh_frame, text="Tên App").grid(row=0, column=0)
tenapp = ttk.Entry(input_hh_frame)
tenapp.grid(row=0, column=1)

ttk.Label(input_hh_frame, text="Tên Đăng Nhập").grid(row=1, column=0)
tendnh = ttk.Entry(input_hh_frame)
tendnh.grid(row=1, column=1)

ttk.Label(input_hh_frame, text="Mật Khẩu").grid(row=2, column=0)
matkhau = ttk.Entry(input_hh_frame)
matkhau.grid(row=2, column=1)

ttk.Label(input_hh_frame, text="Chủ Tài Khoản").grid(row=3, column=0)
chutk = ttk.Entry(input_hh_frame)
chutk.grid(row=3, column=1)

ttk.Label(input_hh_frame, text="Tình Trạng").grid(row=4, column=0)
tinhtrang = ttk.Entry(input_hh_frame)
tinhtrang.grid(row=4, column=1)

load_account_data(tree)
root.mainloop()
