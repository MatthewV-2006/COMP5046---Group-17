import tkinter as tk
from tkinter import ttk
from medicationsDB import add_med_to_db

# opens a new window called 'Add Medication'
def open_add_med(Parent, schedule_list, med_reminders):
    add_med_window = tk.Toplevel(Parent)
    add_med_window.title("Add Medication")
    add_med_window.geometry("650x650")

    
    ttk.Label(add_med_window, text="Add Medication", font = ("Arial", 16)).pack(pady=15)
    
    # Add Medication field
    ttk.Label(add_med_window, text="Medication Name").pack(pady=5)
    name_entry = ttk.Entry(add_med_window)
    name_entry.pack(pady=7)

    # dose amount field
    ttk.Label(add_med_window, text="Dose").pack()
    dose_entry = ttk.Entry(add_med_window)
    dose_entry.pack(pady=5)
    
    # set reminder time text field
    ttk.Label(add_med_window, text="Set Reminder Time (HH:MM)").pack()
    time_entry = ttk.Entry(add_med_window)
    time_entry.pack(pady=5)
    
    # saves medication to medications database
    def save_med():
        
        # reads values entered by the user
        name = name_entry.get()
        dose = dose_entry.get()
        time = time_entry.get()
        
        add_med_to_db(name, dose, time)
        
        med_reminders.append((name, time))
        schedule_list.insert(tk.END, f"{time} - {name}")
        
        # closes window once user has clicked 'Save'
        add_med_window.destroy()

    ttk.Button(add_med_window, text="Save", command=save_med).pack(pady=10)