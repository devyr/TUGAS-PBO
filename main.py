
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="retail_db"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

class RetailApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Retail Management System")
        self.root.geometry("800x600")
        self.create_tables()
        self.main_menu()

    def create_tables(self):
        self.db.execute_query("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10,2) NOT NULL
        )
        """)
        self.db.execute_query("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            quantity INT NOT NULL,
            total_price DECIMAL(10,2) NOT NULL,
            transaction_date DATE NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
        """)

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Retail Management System", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Manage Products", command=self.manage_products, width=30).pack(pady=10)
        tk.Button(self.root, text="Record Transactions", command=self.record_transaction, width=30).pack(pady=10)
        tk.Button(self.root, text="View Transactions", command=self.view_transactions, width=30).pack(pady=10)

    def manage_products(self):
        # Product management implementation here

    def record_transaction(self):
        # Transaction recording implementation here

    def view_transactions(self):
        # Transaction viewing implementation here

if __name__ == "__main__":
    root = tk.Tk()
    app = RetailApp(root)
    root.mainloop()
