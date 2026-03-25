import tkinter as tk
from tkinter import ttk
import sqlite3

class ViewChildMedications:
    def __init__(self, root):
        self.root = root
    
    def create_window(self):
        child_med_window = tk.Toplevel(self.root)
        child_med_window.title("Child medications")
        child_med_window.geometry("850x850")
        
        tree = ttk.Treeview(child_med_window, columns=("Child", "Medication", "Dose", "Time"), show='headings')
        tree.heading("Child", text="Child")
        tree.heading("Medication", text="Medication")
        tree.heading("Dose", text="Dose")
        tree.heading("Time", text="Time")
        tree.pack(fill="both", expand=True)
        
        with sqlite3.connect('Details.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT AccountID, Username FROM AccountDetails WHERE isAdmin = 0")
            children = cursor.fetchall()
    
        with sqlite3.connect('medications.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT child_ID, name, dose, reminder_time FROM medications")
            medications = cursor.fetchall()
        
        for child in children:
            child_id = child[0]
            child_name = child[1]
            
            for med in medications:
                if med[0] == child_id:
                    tree.insert("", tk.END, values=(child_name, med[1], med[2], med[3]))