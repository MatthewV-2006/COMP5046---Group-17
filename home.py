import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3
class home:
    def __init__(self, root):
        #removes tkinter elements from previous page
        for child in root.winfo_children():
            child.destroy()

        self.total_num_medication = 3
        self.taken_meds = 0

        # sets the title of the window
        root.title("Home page")

        # sets the size of the window
        root.geometry("850x850")

        # creates dictionary that stores data about a medication
        self.next_due_medication = {
            "name": "Ibuprofen",
            "dose": "500mg", 
            "time": "10:00"
        }
        # example medication data

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

    # changes the label text when the 'Mark as Taken' button is clicked
    def taken_medication(self,progress_bar,medication_progress_label,status_label):
        self.taken_meds += 1
        progress_bar["value"] = self.taken_meds
        medication_progress_label.config(text=f"{self.taken_meds} / {self.total_num_medication} medications taken")
        status_label.config(text="Medication Taken")
    
    def main(self,root,userDetails):
        # canvas to display everything
        canvas = tk.Canvas(root, scrollregion=(0,0,800,800))
        canvas.pack(anchor=tk.CENTER, expand=True)

        #main frame
        overview_frame = ttk.LabelFrame(canvas, text = "Today's Medication Overview", padding=20)

        #creates a scrollbar for navigating the window
        scrollbar = ttk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side="right",fill="y")
        scrollbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)

        # creates a section box inside the window
        overview_frame.pack(padx=20, pady=20, fill="x",expand=True)

        # displays the medication name
        name_label = ttk.Label(overview_frame, text = f"Medication: {self.next_due_medication['name']}", font = ("Arial", 12))
        name_label.pack(anchor="w", pady=2)

        # displays the dosage of medication
        dose_label = ttk.Label(overview_frame, text = f"Take at: {self.next_due_medication['time']}", font = ("Arial", 12))
        dose_label.pack(anchor="w", pady=2)

        # displays the time at which the medication needs to be taken
        time_label = ttk.Label(overview_frame, text = f"Take at: {self.next_due_medication['time']}", font = ("Arial", 12))
        time_label.pack(anchor="w", pady=2)

        # Button to click on if medication has been taken
        taken_medication_button = ttk.Button(overview_frame, text = "Mark as Taken", command=lambda: self.taken_medication(progress_bar, medication_progress_label,status_label))
        taken_medication_button.pack(pady = 10)

        status_label = ttk.Label(overview_frame, text = "")
        status_label.pack()


        # Today's schedule for medication
        medication_schedule_frame = ttk.LabelFrame(canvas, text = "Today's Schedule:", padding = 10)
        medication_schedule_frame.pack(padx=20, pady=10, fill="both",expand=True)

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
        medication_options = ttk.LabelFrame(canvas, text = "Medication Options:", padding=10)

        # places the section box in the window
        medication_options.pack(padx=20, pady=20, fill="x")

        # creates medication button
        ttk.Button(medication_options, text="Add Medication", command=self.add_medication).pack(fill="x", pady=4)

        # creates edit medication button
        ttk.Button(medication_options, text="Edit Medication", command=self.modify_medication).pack(fill="x", pady=4)

        # creates set reminder button
        ttk.Button(medication_options, text="Set Reminder", command=self.set_medication_reminder).pack(fill="x", pady=4)

        # creates view history button
        ttk.Button(medication_options, text="View History", command=self.view_history).pack(fill="x", pady=4)

        # creates section box called 'Today's Medication Progress:'
        medication_progress_frame = ttk.LabelFrame(canvas, text = "Today's Medication Progress:", padding=10)

        # places section box in the window
        medication_progress_frame.pack(padx=20, pady=20, fill="x",expand=True)

        # creates a text label that displays the total number of medication taken 
        medication_progress_label = ttk.Label(medication_progress_frame, text = f"{self.taken_meds} / {self.total_num_medication} medications taken")

        # places label inside the frame
        medication_progress_label.pack(pady=5)

        """creates progress bar which becomes full
        when number of medication taken is equal
        to total number of medications 
        """
        progress_bar = ttk.Progressbar(medication_progress_frame, length=800, maximum=self.total_num_medication)
        progress_bar.pack(pady=5)

        # displays details of users if the user has admin
        if userDetails[3]:
            #creates new section for user accounts
            users = ttk.LabelFrame(canvas, text = "Users:", padding=10)
            users.pack(padx=20, pady=20, fill="x",expand=True)
            user_list = tk.Listbox(users)
            user_list.pack(fill="both")

            #retrieves details of existing users
            sql = "SELECT AccountID, username, isAdmin FROM AccountDetails"
            with sqlite3.connect('Details.db') as conn:
                cur = conn.cursor()
                cur.execute(sql,)
                iterator = cur.fetchall()
                for row in iterator:
                    print(row)
                    user_list.insert(tk.END, str(row))

        # starts the program and keeps the window open
        root.mainloop()