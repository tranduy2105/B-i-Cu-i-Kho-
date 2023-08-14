import tkinter as tk
from tkinter import ttk
import json

DATA_FILE = "financial_data.json"

class FinancialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Sổ Thu Chi")

        self.transactions = []

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Sổ Thu Chi")
        self.label.pack(pady=10)

        self.date_label = ttk.Label(self.root, text="Ngày:")
        self.date_label.pack()
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.pack()

        self.type_label = ttk.Label(self.root, text="Loại (Thu/Chi):")
        self.type_label.pack()
        self.type_entry = ttk.Entry(self.root)
        self.type_entry.pack()

        self.description_label = ttk.Label(self.root, text="Mô tả:")
        self.description_label.pack()
        self.description_entry = ttk.Entry(self.root)
        self.description_entry.pack()

        self.amount_label = ttk.Label(self.root, text="Số tiền:")
        self.amount_label.pack()
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.pack()

        self.add_button = ttk.Button(self.root, text="Thêm Giao Dịch", command=self.add_transaction)
        self.add_button.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("date", "type", "description", "amount"))
        self.tree.heading("#1", text="Ngày")
        self.tree.heading("#2", text="Loại")
        self.tree.heading("#3", text="Mô tả")
        self.tree.heading("#4", text="Số tiền")
        self.tree.pack()

        self.load_data()

    def add_transaction(self):
        date = self.date_entry.get()
        transaction_type = self.type_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        self.transactions.append({
            "date": date,
            "type": transaction_type,
            "description": description,
            "amount": amount
        })

        self.update_treeview()
        self.save_data()

        self.clear_entries()

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for transaction in self.transactions:
            self.tree.insert("", "end", values=(transaction["date"], transaction["type"], transaction["description"], transaction["amount"]))

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.transactions, file)

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as file:
                self.transactions = json.load(file)
                self.update_treeview()
        except FileNotFoundError:
            pass

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialApp(root)
    root.mainloop()
