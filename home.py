import tkinter as tk
from tkinter import ttk
from datetime import datetime

total_num_medication = 3
taken_meds = 0

# creates the main window
root = tk.Tk()

# sets the title of the window
root.title("Home page")

# sets the size of the window
root.geometry("850x850")

# creates dictionary that stores data about a medication
next_due_medication = {
    "name": "Ibuprofen",
    "dose": "500mg", 
    "time": "10:00"
}
# example medication data

# changes the label text when the 'Mark as Taken' button is clicked
def taken_medication():
    global taken_meds
    taken_meds += 1
    progress_bar["value"] = taken_meds
    medication_progress_label.config(text=f"{taken_meds} / {total_num_medication} medications taken")
    status_label.config(text="Medication Taken")

# main frame
overview_frame = ttk.LabelFrame(root, text = "Today's Medication Overview", padding=20)

# creates a section box inside the window
overview_frame.pack(padx=20, pady=20, fill="x")

# displays the medication name
name_label = ttk.Label(overview_frame, text = f"Medication: {next_due_medication['name']}", font = ("Arial", 12))
name_label.pack(anchor="w", pady=2)

# displays the dosage of medication
dose_label = ttk.Label(overview_frame, text = f"Take at: {next_due_medication['time']}", font = ("Arial", 12))
dose_label.pack(anchor="w", pady=2)

# displays the time at which the medication needs to be taken
time_label = ttk.Label(overview_frame, text = f"Take at: {next_due_medication['time']}", font = ("Arial", 12))
time_label.pack(anchor="w", pady=2)

# Button to click on if medication has been taken
taken_medication_button = ttk.Button(overview_frame, text = "Mark as Taken", command= taken_medication)
taken_medication_button.pack(pady = 10)

status_label = ttk.Label(overview_frame, text = "")
status_label.pack()


# Today's schedule for medication
medication_schedule_frame = ttk.LabelFrame(root, text = "Today's Schedule:", padding = 10)
medication_schedule_frame.pack(padx=20, pady=10, fill="both")

medication_schedule_list = tk.Listbox(medication_schedule_frame)
medication_schedule_list.pack(fill="both")

# example medication data
medication_schedule = [
    "10:00 - Ibuprofen", 
    "14:00 - Iron supplements", 
    "20:00 - Vitamin A"
]

for medication in medication_schedule:
    medication_schedule_list.insert(tk.END, medication)

# creates section box inside the window called 'Medication Options'
medication_options = ttk.LabelFrame(root, text = "Medication Options:", padding=10)

# places the section box in the window
medication_options.pack(padx=20, pady=20, fill="x")

# add medication
def add_medication():
    print("Add medication clicked")

# edit medication
def modify_medication():
    print("Modify medication clicked")

# set remainder for medication
def set_medication_reminder():
    print("set medication reminder clicked")

# view history
def view_history():
    print("view history clicked")

# creates medication button
ttk.Button(medication_options, text="Add Medication", command=add_medication).pack(fill="x", pady=4)

# creates edit medication button
ttk.Button(medication_options, text="Edit Medication", command=modify_medication).pack(fill="x", pady=4)

# creates set reminder button
ttk.Button(medication_options, text="Set Reminder", command=set_medication_reminder).pack(fill="x", pady=4)

# creates view history button
ttk.Button(medication_options, text="View History", command=view_history).pack(fill="x", pady=4)

# creates section box called 'Today's Medication Progress:'
medication_progress_frame = ttk.LabelFrame(root, text = "Today's Medication Progress:", padding=10)

# places section box in the window
medication_progress_frame.pack(padx=20, pady=20, fill="x")

# creates a text label that displays the total number of medication taken 
medication_progress_label = ttk.Label(medication_progress_frame, text = f"{taken_meds} / {total_num_medication} medications taken")

# places label inside the frame
medication_progress_label.pack(pady=5)

"""creates progress bar which becomes full
when number of medication taken is equal
to total number of medications 
"""
progress_bar = ttk.Progressbar(medication_progress_frame, length=800, maximum=total_num_medication)
progress_bar.pack(pady=5)

# starts the program and keeps the window open
root.mainloop()