import tkinter as tk
from tkinter import ttk
from datetime import datetime
from add_medication import open_add_med
from tkinter import messagebox
from medicationsDB import get_med_db

def open_home_page():
    
    total_num_medication = 3
    taken_meds = 0
    medication_reminders = []

    root = tk.Tk() # creates the main window
    root.title("Home page") # sets the title of the window
    root.geometry("650x650") # sets the size of the window

    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand = True)

    scroll_bar = ttk.Scrollbar(root, orient = "vertical", command=canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scroll_bar.set)

    scroll_bar_frame = ttk.Frame(canvas)
    window_id = canvas.create_window((0,0), window=scroll_bar_frame, anchor="nw")

    scroll_bar_frame.columnconfigure(0, weight=1)

    def configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_bar_frame.bind("<Configure>", configure_scroll_region)

    def resizable_frame(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", resizable_frame)
    
    # changes the label text when the 'Mark as Taken' button is clicked
    def taken_medication():
        nonlocal taken_meds
        taken_meds += 1
        progress_bar["value"] = taken_meds
        medication_progress_label.config(text=f"{taken_meds} / {total_num_medication} medications taken")
        status_label.config(text="Medication Taken")
    
    def check_reminders():
        current_time = datetime.now().strftime("%H:%M")
        
        for med, time_set in medication_reminders:
            if current_time == time_set:
                messagebox.showinfo("Medication Reminder", f"Time to take {med}")
        
        root.after(60000, check_reminders)
                
    # sorts reminders and retrieves the earliest medication 
    def get_due_medication():
        now = datetime.now()
        medications = []
        for med, reminder_time in medication_reminders:
            medication_reminder_time = datetime.strptime(reminder_time, "%H:%M")
            medication_reminder_time = medication_reminder_time.replace(year=now.year, month=now.month, day=now.day)
            medications.append((med, medication_reminder_time))
        
        medications.sort(key=lambda x: x[1])
            
        for med, reminder_time in medications:
            if reminder_time >= now:
                return med, reminder_time.strftime("%H:%M")
        
        if medications:
            med, reminder_time = medications[0]
            return med, reminder_time.strftime("%H:%M")
        
        return None, None
    
    # add medication
    def add_med():
        open_add_med(root, medication_schedule_list, medication_reminders)
        
    # edit medication
    def modify_medication():
        print("Modify medication clicked")

    # set remainder for medication
    def set_medication_reminder():
        print("set medication reminder clicked")

    # view history
    def view_history():
        print("view history clicked")
    
    
    # main frame
    overview_frame = ttk.LabelFrame(scroll_bar_frame, text = "Today's Medication Overview", padding=20)

    # creates a section box inside the window
    overview_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    # Today's schedule for medication
    medication_schedule_frame = ttk.LabelFrame(scroll_bar_frame, text = "Today's Schedule:", padding = 10)
    medication_schedule_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

    medication_schedule_list = tk.Listbox(medication_schedule_frame)
    medication_schedule_list.pack(fill="both")

    rows = get_med_db()
    for name, dose, reminder_time in rows:
        medication_schedule_list.insert(tk.END, f"{reminder_time} - {name}")
        medication_reminders.append((name, reminder_time))      
    
    next_due_medication = get_due_medication()
    name_of_med, reminder_time = next_due_medication
    
    if name_of_med:
        name_text = f"Medication: {name_of_med}"
    else:
        name_text = "Medication: None"
    
    if reminder_time:
        time_text = f"Take at: {reminder_time}"
    else:
        time_text = f"Take at: --"
    
    
    # displays the medication name
    name_label = ttk.Label(overview_frame, text = name_text, font = ("Arial", 12))
    name_label.pack(anchor="w", pady=2)

    # displays the dosage of medication
    dose_label = ttk.Label(overview_frame, text = f"Dose:", font = ("Arial", 12))
    dose_label.pack(anchor="w", pady=2)

    # displays the time at which the medication needs to be taken
    time_label = ttk.Label(overview_frame, text = time_text, font = ("Arial", 12))
    time_label.pack(anchor="w", pady=2)

    # Button to click on if medication has been taken
    taken_medication_button = ttk.Button(overview_frame, text = "Mark as Taken", command= taken_medication)
    taken_medication_button.pack(pady = 10)

    status_label = ttk.Label(overview_frame, text = "")
    status_label.pack()

    # creates section box inside the window called 'Medication Options'
    medication_options = ttk.LabelFrame(scroll_bar_frame, text = "Medication Options:", padding=10)

    # places the section box in the window
    medication_options.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # creates medication button
    ttk.Button(medication_options, text="Add Medication", command=add_med).pack(fill="x", pady=4)

    # creates edit medication button
    ttk.Button(medication_options, text="Edit Medication", command=modify_medication).pack(fill="x", pady=4)

    # creates set reminder button
    ttk.Button(medication_options, text="Set Reminder", command=set_medication_reminder).pack(fill="x", pady=4)

    # creates view history button
    ttk.Button(medication_options, text="View History", command=view_history).pack(fill="x", pady=4)

    # creates section box called 'Today's Medication Progress:'
    medication_progress_frame = ttk.LabelFrame(scroll_bar_frame, text = "Today's Medication Progress:", padding=10)

    # places section box in the window
    medication_progress_frame.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    # creates a text label that displays the total number of medication taken 
    medication_progress_label = ttk.Label(medication_progress_frame, text = f"{taken_meds} / {total_num_medication} medications taken")

    # places label inside the frame
    medication_progress_label.pack(pady=5)

    """creates progress bar which becomes full when number of medications taken is equal
    to total number of medications so it allows the user to track their progress
    """
    progress_bar = ttk.Progressbar(medication_progress_frame, maximum=total_num_medication)
    progress_bar.pack(fill="x", pady=5)
    
    check_reminders()
    root.mainloop()  # starts the program and keeps the window open