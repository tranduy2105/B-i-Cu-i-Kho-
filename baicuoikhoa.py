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

        self.tree = ttk.Treeview(self.root, columns=("index", "date", "type", "description", "amount"))
        self.tree.heading("#1", text="STT")
        self.tree.heading("#2", text="Ngày")
        self.tree.heading("#3", text="Loại")
        self.tree.heading("#4", text="Mô tả")
        self.tree.heading("#5", text="Số tiền")
        self.tree.pack()

        self.load_data()

        self.find_history_label = ttk.Label(self.root, text="Tìm lịch sử giao dịch theo ngày:")
        self.find_history_label.pack()
        self.find_history_entry = ttk.Entry(self.root)
        self.find_history_entry.pack()

        self.find_history_button = ttk.Button(self.root, text="Tìm lịch sử", command=self.find_history)
        self.find_history_button.pack()

        self.delete_history_button = ttk.Button(self.root, text="Xoá lịch sử giao dịch", command=self.delete_history)
        self.delete_history_button.pack()

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

    def find_history(self):
        date = self.find_history_entry.get()
        matching_indices = []
        for index, transaction in enumerate(self.transactions):
            if date in transaction["date"]:
                matching_indices.append(index)
        self.highlight_matching_indices(matching_indices)

    def highlight_matching_indices(self, indices):
        self.tree.selection_remove(self.tree.get_children())
        for index in indices:
            item = self.tree.get_children()[index]
            self.tree.selection_add(item)

    def delete_history(self):
        selected_items = self.tree.selection()
        indices_to_delete = []
        for item in selected_items:
            index = int(self.tree.item(item, "text")) - 1
            indices_to_delete.append(index)
        self.delete_transactions(indices_to_delete)
        self.clear_selection()

    def delete_transactions(self, indices):
        indices.sort(reverse=True)
        for index in indices:
            del self.transactions[index]
        self.save_data()
        self.update_treeview()

    def clear_selection(self):
        self.tree.selection_remove(self.tree.selection())

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for index, transaction in enumerate(self.transactions, start=1):
            self.tree.insert("", "end", text=index, values=(index, transaction["date"], transaction["type"], transaction["description"], transaction["amount"]))

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
        self.find_history_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialApp(root)
    root.mainloop()
